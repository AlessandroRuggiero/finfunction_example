import extism

@extism.plugin_fn
def run():
  params = extism.input_json()
  extism.output_str(f"Hello from finfunc! params: {params}")