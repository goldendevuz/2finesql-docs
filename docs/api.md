# API Reference

## `Database`
- `create(table)` → Creates a table.
- `save(instance)` → Inserts a record.
- `all(table)` → Returns all records.
- `get(table, id)` → Get record by id.
- `get_by_field(table, field_name, value)` → LIKE search by field.
- `update(instance)` → Updates a record.
- `delete(table, id)` → Deletes a record.

## `Table`
- Base class for all models.
- Automatically provides `id` field.
- Column and ForeignKey definitions supported.

## `Column`
- Define a typed column (`int`, `str`, `float`, `bool`, `bytes`).

## `ForeignKey`
- Define foreign key to another table.

### Column Types

| Type | SQLite | Description |
|------|--------|-------------|
| `str` | TEXT | String data |
| `int` | INTEGER | Integer numbers |
| `float` | REAL | Floating-point numbers |
| `bool` | INTEGER | Boolean values |
| `bytes` | BLOB | Binary data |
