"""Optional: HTTP trigger for Cloud Scheduler -> run same job logic."""

from datetime import datetime, timezone

from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Schedule Trigger API")

# Set SCHEDULER_SECRET in env; Cloud Scheduler sends header X-Scheduler-Token
EXPECTED = __import__("os").getenv("SCHEDULER_SECRET", "change-me")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/jobs/run")
def run_scheduled_job(x_scheduler_token: str | None = Header(None)):
    if x_scheduler_token != EXPECTED:
        raise HTTPException(status_code=403, detail="invalid scheduler token")

    from run_job import write_report

    path = write_report("success", "triggered via HTTP /jobs/run")
    return {
        "message": "job executed",
        "utc": datetime.now(timezone.utc).isoformat(),
        "report": str(path.name),
    }


# uvicorn trigger_api:app --host 0.0.0.0 --port 8010
# Cloud Scheduler: POST https://YOUR_URL/jobs/run  Header: X-Scheduler-Token: secret