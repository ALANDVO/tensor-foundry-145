"""
Tensor Foundry-145 API Server
FastAPI backend for the terminal window manager
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import uvicorn
from datetime import datetime

app = FastAPI(
    title="Tensor Foundry-145 API",
    description="Terminal window manager API for agent orchestration",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data store (persists across requests within the same process)
panes_store: Dict[str, dict] = {}
workspaces_store: Dict[str, dict] = {}
sessions_store: Dict[str, dict] = {}

# Basic data models
class PaneData(BaseModel):
    id: str
    title: str
    content: Optional[str] = None
    x: int = 0
    y: int = 0
    width: int = 80
    height: int = 24

    class Config:
        schema_extra = {
            "example": {
                "id": "pane-1",
                "title": "Terminal Pane",
                "content": "Terminal output",
                "x": 0,
                "y": 0,
                "width": 80,
                "height": 24
            }
        }

class WorkspaceData(BaseModel):
    id: str
    name: str
    panes: List[PaneData] = []
    active_pane: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": "workspace-1",
                "name": "Main Workspace",
                "panes": [],
                "active_pane": "pane-1"
            }
        }

class SessionData(BaseModel):
    id: str
    name: str
    workspaces: List[WorkspaceData] = []
    current_workspace: Optional[str] = None
    created_at: datetime = datetime.now()
    last_updated: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "id": "session-1",
                "name": "Development Session",
                "workspaces": [],
                "current_workspace": "workspace-1"
            }
        }

# API Routes
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Tensor Foundry-145 API",
        "version": "0.1.0",
        "description": "Terminal window manager for agent orchestration"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}

@app.get("/api/v1/panes")
async def get_panes():
    """Get all panes"""
    pane_list = list(panes_store.values())
    return {"panes": pane_list, "count": len(pane_list)}

@app.get("/api/v1/panes/{pane_id}")
async def get_pane(pane_id: str):
    """Get specific pane by ID"""
    pane = panes_store.get(pane_id)
    if pane is None:
        return {"pane_id": pane_id, "data": {}}
    return {"pane_id": pane_id, "data": pane}

@app.post("/api/v1/panes")
async def create_pane(pane: PaneData):
    """Create new pane"""
    pane_id = pane.id
    panes_store[pane_id] = pane.model_dump()
    return {"status": "created", "pane_id": pane_id}

@app.delete("/api/v1/panes/{pane_id}")
async def delete_pane(pane_id: str):
    """Delete pane"""
    panes_store.pop(pane_id, None)
    return {"status": "deleted", "pane_id": pane_id}

@app.get("/api/v1/workspaces")
async def get_workspaces():
    """Get all workspaces"""
    ws_list = list(workspaces_store.values())
    return {"workspaces": ws_list, "count": len(ws_list)}

@app.get("/api/v1/workspaces/{workspace_id}")
async def get_workspace(workspace_id: str):
    """Get specific workspace by ID"""
    ws = workspaces_store.get(workspace_id)
    if ws is None:
        return {"workspace_id": workspace_id}
    return {"workspace_id": workspace_id, "data": ws}

@app.post("/api/v1/workspaces")
async def create_workspace(workspace: WorkspaceData):
    """Create new workspace"""
    ws_id = workspace.id
    workspaces_store[ws_id] = workspace.model_dump()
    return {"status": "created", "workspace_id": ws_id}

@app.get("/api/v1/sessions")
async def get_sessions():
    """Get all sessions"""
    sess_list = list(sessions_store.values())
    return {"sessions": sess_list, "count": len(sess_list)}

@app.post("/api/v1/sessions")
async def create_session(session: SessionData):
    """Create new session"""
    sess_id = session.id
    sessions_store[sess_id] = session.model_dump()
    return {"status": "created", "session_id": sess_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
