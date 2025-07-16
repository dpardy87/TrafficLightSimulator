# Traffic Light Simulator

A terminal-based Python program that simulates a traditional traffic light using colored ASCII art. The user is prompted to enter the duration for each light (red, yellow, green), and the program cycles through the lights indefinitely until the user types `exit`.

---

## 🚦 Features

- Custom duration input for each light
- Color-coded ASCII representation of traffic lights
- Live terminal updates with screen clearing
- Graceful exit support via `exit` or `Ctrl+C`
- Lightweight and dependency-free

---

## 🛠 How It Works

1. The user is prompted to enter a duration (in seconds) for each light color.
2. The simulator loops through RED → YELLOW → GREEN, clearing the screen between transitions.
3. A separate background thread monitors for the keyword `exit` and stops the simulation when typed.

---

## ▶️ Usage

### 🐳 Running with Docker

Build and run the simulator using Docker for isolated, portable execution.

> 💡 **Don't have Docker installed?**
> You can download it from the official site:
> 👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

1. Build the Docker Image:

```bash
docker build -t traffic-light-sim .
```

2. Run the container:

```bash
docker run -it traffic-light-sim
```

### Run all tests from project root:

```bash
python tests/test_traffic_light.py
```

or

```bash
pytest tests/
```