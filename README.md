# Tensor Foundry-145

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


A terminal window manager that knows what your agents are doing.

## Overview

Tensor Foundry-145 is a sophisticated terminal multiplexer with AI/ML integration. It provides:
- **Tiling panes** with intelligent layout management
- **Workspaces** for organizing terminal sessions
- **Sessions** that survive restarts and preserve state
- **One Inbox** for every coding agent with automatic hook integration

## Technology Stack

- **Backend**: FastAPI (Python) - High-performance REST API
- **Frontend**: React (JavaScript/TypeScript) - Modern, responsive UI
- **CLI**: Go (Golang) - Command-line interface and session management
- **Architecture**: Modular, component-based design with dependency injection

## Getting Started

### Prerequisites
- Python 3.8+ with FastAPI support
- Go 1.20+ for CLI tools
- Node.js 18+ for frontend development

### Installation

```bash
# Clone repository
git clone <repository-url>
cd tensor-foundry-145

# Install dependencies
# Backend
pip install -r api/requirements.txt
# Frontend  
cd client && npm install
# CLI (Go modules)
cd cmd/tuios && go mod init tuios
go mod tidy
```

### Basic Usage

1. **Start the API server**
   ```bash
   cd api
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. **Start the frontend**
   ```bash manufactory
   cd client
   npm run dev
   ```

3. **CLI management**
   ```bash
   # Check status
   tuios list-sessions
   
   # Create new session
   tuios create-session --name "development"
   
   # Run commands in panes
   tuios run "ls -la"
   ```

### API Endpoints

- **Health Check**: `GET /api/v1/health`
- **Panes**: `GET /api/v1/panes`, `POST /api/v1/panes`
- **Workspaces**: `GET /api/v1/workspaces`, `POST /api/v1/workspaces`
- **Sessions**: `GET /api/v1/sessions`, `POST /api/v1/sessions`

## Architecture

### Backend (FastAPI)
The FastAPI server provides:
- RESTful API for pane and workspace management
- Session persistence and state management
- Agent integration through hook endpoints
- WebSocket support for real-time updates

### Frontend (React)
The React application offers:
- Responsive, material design UI
- Real-time dashboard with agent status
- Workspace and pane management interface
- Command palette and keybinding configuration

### CLI (Go)
The Go CLI provides:
- Command-line session management
- Pane manipulation commands
- Session creation and restoration
- Agent integration controls

## Features

### Core Features
- **Intelligent tiling** with responsive layouts
- **Smart workspaces** with tab-based organization
- **Persistent sessions** across restarts
- **Agent integration** with automatic inbox

### AI/ML Integration
- **Agent awareness** for context-aware pane management
- **Hook-based integration** for agent events
- **Intelligent focus management** based on agent activity
- **Code completion** and agent collaboration tools

### Advanced Features
- **Multi-language support** (English, French)
- **Theming engine** with accent-ground styling
- **Help mode** with contextual documentation
- **Privacy mode** for masking sensitive output

## Development

### Development Workflow
1. **Testing**: Comprehensive unit, integration, and end-to-end testing
2. commutationl coding: Branch-based development with peer review
3. **Documentation**: Live documentation with contextual help
4. **Iteration**: Small, focused PRs for each feature

### Code Organization
```
.
├── api/                    # FastAPI backend
│   ├── main.py           # Main API server
│   └── tests/           # API tests
├── client/               # React frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── pages/       # Page components
│   │   └── main.jsx     # App entry point
│   ├── vite.config.js   # Build configuration
│   └── package.json     # Dependencies
├── cmd/tuios/            # Go CLI interface
│   └── main.go          # CLI entrypoint
├── internal/             # Internal packages
│   ├── workspace/       # Workspace management
│   ├── pane/            # Pane management
│   └── session/         # Session handling
└── docs/                 # Documentation
    └── api.md           # API documentation
```

### Testing Strategy
- **Unit tests**: Individual component testing
- **Integration tests**: API and system integration
- **End-to-end tests**: Real user workflows
- **Performance tests**: Load and stress testing

## Configuration

### Config.toml
The main configuration file supports:
```toml
[ui]
language = "en"           # UI language
theme = "default"        # Color theme
default_layout = "master-stack"  # Default pane layout

[appearance]
dock_position = "top"    # Dock positioning
pane_border = true       # Show pane borders
show_agent_icons = true  # Display agent status icons

[keybindings]
default_leader = "ctrl+a"  # Command leader key
help_key = "h"             # Help toggle key
workspace_switch_key = "ctrl+tab"  # Workspace navigation

[agent]
inbox_path = "~/.codex/inbox"  # Agent inbox location
auto_connect = true           # Auto-connect agent servers
max_concurrent_agents = 5     # Maximum agents

[privacy]
enabled = false             # Privacy mask mode
mask_patterns = ["secret", "email", "phone", "card", "iban", "ip"]
allow_hosts = ["github.com", "learn.microsoft.com"]  # Exceptions
```

## Deployment

### Docker
```bash
# Build Docker image
docker build -t tensor-foundry-145 .

# Run with development mode
docker run -p 8000:8000 -p 3000:3000 tensor-foundry-145:dev

# Production mode
docker run -d -p 8000:8000 --name tensor-foundry-145 tensor-foundry-145:latest
```

### Development Server
```bash
# Start all services with docker-compose
docker-compose up -d

# Individual services
docker exec -it tensor-foundry-145_api /bin/bash
docker exec -it tensor-foundry-145_client /bin/bash
```

## Security

Tensor Foundry-145 includes:
- **Input validation** on all API endpoints
- **Rate limiting** for API endpoints
- **WebSocket security** for real-time updates
- **Session isolation** and encryption
- **Privacy mode** for sensitive data masking

## Contact

- **Website**: https://tuios.dev
- **GitHub**: https\-github.com/ALANDVO/tensor-foundry-145
- **Documentation**: Available in `/docs/` directory
- **Issues**: Submit through GitHub issues tracker

## License

Tensor Foundry-145 is an MIT-licensed open-source project. Commercial use is permitted with attribution.

## Development Roadmap

### Phase 1: Initial Setup (Current)
- [x] Repository structure creation
- [x] Basic CLI entrypoint
- [x] FastAPI backend skeleton
- [x] React frontend skeleton

### Phase 2: Core Implementation (Next)
- [ ] Workspace and pane management (internal/workspace.go, internal/pane.go)
- [ ] Session persistence and state management
- [ ] Terminal emulation foundation
- [ ] Agent integration hooks
- [ ] UI components (Command palette, Dock, Rails)

### Phase 3: Advanced Features (Future)
- Help mode and contextual documentation
- Privacy masking for sensitive output
- Theme and language support
- Advanced pane management

## Current Status

**Development Phase**: INITIAL_SETUP_COMPLETE
**Current Feature**: Repository structure and basic foundation
**Status**: Ready for implementation of core workspace and pane management
**Next Steps**: Implement internal/workspace.go, internal/pane.go, and internal/session.go

## Verification

Run tests to verify functionality:
```bash
# API tests
cd api && python -m pytest tests/

# CLI tests
cd cmd/tuios && go test ./...

# Frontend tests
cd client && npm run test

# End-to-end tests
playwright test
```

For current status and updates, visit the project's GitHub repository and documentation.

Maintainer: Alan Vo <alanvo@gmail.com>

---

Alan Vo · [alanvo.net](https://alanvo.net) · [X: @alanvoasi](https://x.com/alanvoasi)
