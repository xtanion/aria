## Project Structure
```txt
.
├── platformio.ini              # PlatformIO build config
├── src/
│   ├── main.cpp                # Main entry point
│   ├── config.cpp              # Wi-Fi & server config
│   ├── config.h
│   ├── display/
│   │   ├── display_utils.cpp   # OLED display helpers
│   │   └── display_utils.h
│   └── websocket/
│       ├── websocket_client.cpp
│       └── websocket_client.h
```

## Setup
Clone this repo
Install PlatformIO using `pipx` in macOS:
```bash
pipx install platformio
```

`Update Wi-Fi credentials and WebSocket server IP in src/config.cpp`

## PlatformIO Commands
Build firmware
```bash
pio run
```
Upload firmware to ESP32
```bash
pio run --target upload
```

Monitor serial output
```bash
pio device monitor
pio device monitor -p /dev/cu.usbserial-0001  # Or to specify a port manually
```
Notes
Ensure the correct USB serial port is selected, or manually specify upload_port in platformio.ini.

You can use `pio run -t compiledb` to generate compile_commands.json for editor support (e.g., Zed with clangd).
