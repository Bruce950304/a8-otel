from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
provider.add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("a8.demo")

with tracer.start_as_current_span("checkout"):          # parent
    with tracer.start_as_current_span("charge-card"):   # child
        print("paid")