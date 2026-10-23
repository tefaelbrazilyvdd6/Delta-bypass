import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uvicorn

if __name__ == "__main__":
    from server import app
    port = int(os.environ.get("PORT", 2233))
    uvicorn.run(app, host="0.0.0.0", port=port)
