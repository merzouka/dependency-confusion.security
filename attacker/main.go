package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main() {
	// Define the handler for the root endpoint
	http.HandleFunc("/", handlePostRequest)

	// Start the server on port 9000
	addr := ":9000"
	fmt.Printf("Server starting on http://localhost%s\n", addr)
	if err := http.ListenAndServe(addr, nil); err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}

func handlePostRequest(w http.ResponseWriter, r *http.Request) {
	// Only allow POST requests
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	// Read the request body
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, fmt.Sprintf("Failed to read request body: %v", err), http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	// // Parse the JSON data
	// var data map[string]interface{}
	// if err := json.Unmarshal(body, &data); err != nil {
	// 	http.Error(w, fmt.Sprintf("Failed to parse JSON: %v", err), http.StatusBadRequest)
	// 	return
	// }

	// Log the received data
	fmt.Printf("%s", body)

	// Send a success response
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "Data received successfully")
}
