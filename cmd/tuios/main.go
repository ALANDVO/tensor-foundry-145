package main

import (
	"fmt"
	"os"
)

func main() {
	// Basic CLI entry point for Tensor Foundry-145
	// A terminal window manager that knows what your agents are doing.

	if len(os.Args) < 2 {
		fmt.Println("Tensor Foundry-145 - Terminal Window Manager")
		fmt.Println("")
		fmt.Println("Usage:")
		fmt.Println("  tuios <command> [options]")
		fmt.Println("")
		fmt.Println("Commands:")
		fmt.Println("  run     Start the terminal window manager")
		fmt.Println("  help    Show help information")
		fmt.Println("")
		fmt.Println("Use 'tuios help <topic>' for more information about a specific topic.")
		return
	}

	command := os.Args[1]
	switch command {
	case "run":
		runCommand()
	case "help":
		helpCommand()
	default:
		fmt.Printf("Unknown command: %s\n", command)
		os.Exit(1)
	}
}

func runCommand() {
	fmt.Println("Tensor Foundry-145 - Starting terminal window manager...")
	fmt.Println("Features:")
	fmt.Println("  - Tiling panes and workspaces")
	fmt.Println("  - Sessions that survive restarts") 
	fmt.Println("  - One Inbox for every coding agent")
	fmt.Println("  - Agent-aware window management")
	fmt.Println("")
	fmt.Println("Note: This is the initial skeleton implementation.")
	fmt.Println("Core workspace and pane management to be implemented in Phase 2.")
	fmt.Println("")
	fmt.Println("Press Ctrl+C to exit")
	
	// For now, just wait for a signal
	select {}
}

func helpCommand() {
	if len(os.Args) >= 3 {
		topic := os.Args[2]
		switch topic {
		case "workspaces":
			fmt.Println("Workspaces:")
			fmt.Println("  - Create named workspaces with tabs")
			fmt.Println("  - Switch between workspaces with Ctrl+Tab")
			fmt.Println("  - Each workspace maintains its own pane layout")
		case "panes":
			fmt.Println("Panes:")
			fmt.Println("  - Split screens into multiple panes")
			fmt.Println("  - Navigate between panes with Ctrl+Arrow keys")
			fmt.Println("  - Each pane can run a different program")
		default:
			fmt.Printf("Unknown help topic: %s\n", topic)
		}
		return
	}
	
	fmt.Println("Tensor Foundry-145 Help")
	fmt.Println("")
	fmt.Println("Available commands:")
	fmt.Println("  tuios run     Start the terminal window manager")
	fmt.Println("  tuios help    Show this help message")
	fmt.Println("")
	fmt.Println("For more information, visit the documentation.")
}
