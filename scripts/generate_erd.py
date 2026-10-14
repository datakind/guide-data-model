#!/usr/bin/env python3
"""Generate an interactive, searchable HTML relationship explorer.

Reads the "Objects" and "ObjectDesc" records of the GUIDE Data Model JSON.

Run from the repo root:
    python scripts/generate_erd.py [model.json] [output.html]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from generate_schema import (
    DEFAULT_MODEL_JSON,
    MODEL_NAME,
    REPO_ROOT,
    SCHEMA_VERSION,
    load_model,
    parse_fk_refs,
    pg_type_for,
    safe_ident,
    schema_name,
    to_snake,
)


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__MODEL_NAME__ __VERSION__ relationship explorer</title>
<style>
:root{color-scheme:dark;--bg:#0d1117;--panel:#161b22;--line:#30363d;--text:#c9d1d9;--muted:#8b949e;--accent:#58a6ff;--key:#e3b341}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 system-ui,sans-serif}
header{padding:16px 20px;border-bottom:1px solid var(--line);background:var(--panel);display:flex;gap:18px;align-items:center;flex-wrap:wrap}
h1{font-size:18px;margin:0}header p{margin:0;color:var(--muted)}.controls{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
input,select{background:var(--bg);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:8px 10px;min-width:220px}
main{display:grid;grid-template-columns:minmax(260px,340px) 1fr;height:calc(100vh - 76px)}
aside{border-right:1px solid var(--line);overflow:auto;padding:10px}.summary{color:var(--muted);padding:4px 8px 10px}
.table-button,.relation{width:100%;text-align:left;background:transparent;color:var(--text);border:0;border-radius:5px;padding:7px 8px;cursor:pointer}
.table-button:hover,.table-button.active,.relation:hover{background:#1f2937;color:#fff}.table-button small{display:block;color:var(--muted)}
article{overflow:auto;padding:24px}h2{margin:0 0 4px;font-size:24px}.schema{color:var(--accent);font-family:ui-monospace,monospace}
.description{max-width:1000px;color:var(--muted);margin:14px 0 20px}.relations{display:grid;grid-template-columns:repeat(2,minmax(240px,1fr));gap:16px;margin-bottom:22px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px}.card h3{margin:0 0 8px;font-size:14px}.relation{color:var(--accent);padding:4px}
table{width:100%;border-collapse:collapse;background:var(--panel);border:1px solid var(--line)}th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{position:sticky;top:0;background:#21262d}
code{font-family:ui-monospace,monospace;color:#79c0ff}.key{color:var(--key);font-weight:700}.empty{color:var(--muted);font-style:italic}@media(max-width:800px){main{grid-template-columns:1fr;height:auto}aside{max-height:38vh;border-right:0;border-bottom:1px solid var(--line)}article{min-height:62vh}.relations{grid-template-columns:1fr}}
</style>
</head>
<body>
<header><div><h1>__MODEL_NAME__ __VERSION__ relationship explorer</h1><p>__TABLE_COUNT__ objects · __COLUMN_COUNT__ columns · __ENTITY_COUNT__ entities</p></div><div class="controls"><input id="search" type="search" placeholder="Search objects or columns"><select id="entity"><option value="">All entities</option></select></div></header>
<main><aside><div class="summary" id="summary"></div><div id="table-list"></div></aside><article id="detail"><p class="empty">Select an object to inspect its columns and relationships.</p></article></main>
<script>
const MODEL=__MODEL_JSON__;
const list=document.getElementById('table-list'),detail=document.getElementById('detail'),search=document.getElementById('search'),entity=document.getElementById('entity'),summary=document.getElementById('summary');
const incoming={};for(const name of Object.keys(MODEL.tables))incoming[name]=[];for(const [source,table] of Object.entries(MODEL.tables))for(const target of table.targets)if(incoming[target])incoming[target].push(source);
const make=(tag,text,cls)=>{const node=document.createElement(tag);if(text!==undefined)node.textContent=text;if(cls)node.className=cls;return node};
for(const item of MODEL.entities){const option=make('option',`${item.name} (${item.count})`);option.value=item.name;entity.append(option)}
let selected='';
function relationButton(name){const button=make('button',name,'relation');button.onclick=()=>show(name);return button}
function relationCard(title,names){const card=make('section',undefined,'card');card.append(make('h3',`${title} (${names.length})`));if(names.length){for(const name of names)card.append(relationButton(name))}else card.append(make('p','None','empty'));return card}
function show(name){selected=name;const table=MODEL.tables[name];detail.replaceChildren();detail.append(make('h2',name));detail.append(make('div',`${table.schema}.${table.sqlName}`,'schema'));detail.append(make('p',table.description||'No object description provided.','description'));const relations=make('div',undefined,'relations');relations.append(relationCard('References',table.targets),relationCard('Referenced by',incoming[name]||[]));detail.append(relations);const grid=make('table');const head=make('thead'),headRow=make('tr');for(const label of ['Column','Type','Key','Nullable','References','Description'])headRow.append(make('th',label));head.append(headRow);grid.append(head);const body=make('tbody');for(const column of table.columns){const row=make('tr');row.append(make('td',column.name));row.append(make('td',column.type));row.append(make('td',column.key||'',column.key?'key':''));row.append(make('td',column.nullable));const refs=make('td');for(const ref of column.references){const code=make('code',ref);refs.append(code,document.createElement('br'))}row.append(refs);row.append(make('td',column.description||''));body.append(row)}grid.append(body);detail.append(grid);renderList()}
function matches(name,table,query){if(!query)return true;const text=[name,table.entity,table.description,...table.columns.flatMap(c=>[c.name,c.description])].join(' ').toLowerCase();return text.includes(query)}
function renderList(){const query=search.value.trim().toLowerCase(),entityName=entity.value;const names=Object.keys(MODEL.tables).filter(name=>{const table=MODEL.tables[name];return(!entityName||table.entity===entityName)&&matches(name,table,query)}).sort();summary.textContent=`${names.length} objects shown`;list.replaceChildren();for(const name of names){const table=MODEL.tables[name],button=make('button',name,'table-button'+(name===selected?' active':''));button.append(make('small',`${table.entity} · ${table.columns.length} columns`));button.onclick=()=>show(name);list.append(button)}}
search.addEventListener('input',renderList);entity.addEventListener('change',renderList);renderList();
</script>
</body>
</html>
"""



def main() -> None:
    json_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MODEL_JSON
    output_path = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else REPO_ROOT / "docs" / "data-model" / "ERD--all_entities.html"
    )
    model_tables, descriptions = load_model(json_path)

    tables = {}
    column_count = 0
    for object_name, info in model_tables.items():
        targets = set()
        columns = []
        for c in info["columns"]:
            column_count += 1
            references = parse_fk_refs(c["fk_ref"]) if c["fk_ref"] else []
            targets.update(r.split(".", 1)[0] for r in references)
            columns.append({
                "name": c["column"],
                "type": pg_type_for(c["column"], c["generic_type"]),
                "key": c["key"],
                "nullable": "No" if c["nullable"] == "N" else "Yes",
                "references": references,
                "description": c["description"],
            })
        tables[object_name] = {
            "entity": info["entity"],
            "schema": schema_name(info["entity"]),
            "sqlName": safe_ident(to_snake(object_name)),
            "description": descriptions.get(object_name, ""),
            "columns": columns,
            "targets": sorted(targets),
        }

    entity_counts = {}
    for table in tables.values():
        entity_counts[table["entity"]] = entity_counts.get(table["entity"], 0) + 1
    model = {
        "version": SCHEMA_VERSION,
        "entities": [{"name": n, "count": c} for n, c in sorted(entity_counts.items())],
        "tables": dict(sorted(tables.items())),
    }
    model_json = json.dumps(model, ensure_ascii=False, separators=(",", ":"))
    model_json = model_json.replace("</", "<\\/")
    html = (
        HTML_TEMPLATE
        .replace("__MODEL_NAME__", MODEL_NAME)
        .replace("__VERSION__", SCHEMA_VERSION)
        .replace("__TABLE_COUNT__", str(len(tables)))
        .replace("__COLUMN_COUNT__", f"{column_count:,}")
        .replace("__ENTITY_COUNT__", str(len(entity_counts)))
        .replace("__MODEL_JSON__", model_json)
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
