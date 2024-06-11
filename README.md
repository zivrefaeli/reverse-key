# `reverse-key` - Custom Fluentd Plugin 🕊️

Following **fluentd** SDK at https://docs.fluentd.org/plugin-development

## Custom `filter` Plugin 🔀

`reverse-key` is a plugin that takes a `record` and reverses one of its values.

To configure the plugin at `fluent.conf`:

```xml
<filter **>
  @type reverse_key
  key level
</filter>
```

This filter takes a record with **key** named `level`, and reverse its value. By default, key equals to "message"

For example,

```python
# Input record
{"datetime":"2024-06-01T22:32:14.774291","level":"ERROR","file":{"name":"main.py","line":44},"message":"Hello Error log","content":[]}

# Output record
{"datetime":"2024-06-01T22:32:14.774291","level":"RORRE","file":{"name":"main.py","line":44},"message":"Hello Error log","content":[]}
```

## Usage

To add the plugin to fluentd, add the file `filter_reverse_key.rb` to `/fluentd/plugins` folder

### Run locally

Using docker-compose with a **FastAPI** app:

```bash
docker compose up --build -d
```