import extism

@extism.plugin_fn
def greet():
  extism.output_str(f"Hello from finfunc!")