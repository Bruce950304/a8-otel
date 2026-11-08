\# Assignment 8: Observability with OpenTelemetry



| Task | Files | What it shows |

|---|---|---|

| 1 (A) | `app.py` | SDK console exporter, parent and child spans |

| 2 (E) | `app\_otlp.py`, `otel-collector-config.yaml` | App -> Dockerized Collector -> console and file |

| 3 (O) | `app\_flask.py`, `otel-collector-task3.yaml` | Auto-instrumented Flask, log-trace correlation |



`out/` holds the telemetry collected during the runs shown in the report.



\## Setup (Windows PowerShell)



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

```



Collector image: `otel/opentelemetry-collector:0.164.0`

