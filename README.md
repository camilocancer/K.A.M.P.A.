# K.A.M.P.A.
> **K**eeping **A**ll **M**emories, **P**rotecting **A**lways.

Currently, this project operates as an advanced terminal-based voice assistant with persistent context memory, live web search capabilities, and robust exception handling. However, the ultimate vision for K.A.M.P.A. is to evolve into a comprehensive, omnipresent assistant capable of managing and automating both digital and physical environments to improve daily life.

## Vision & Purpose
The core objective of K.A.M.P.A. goes beyond mere convenience; it aims to drastically enhance physical and digital security. The system is designed to handle critical real-world scenarios—ranging from detecting health emergencies (such as a family member falling and being unable to call for help) to securing the home against unexpected intrusions.

## Roadmap

- [x] **Phase 1: Core Interface** - Deployment of a simple, terminal-based voice chatbot.
- [x] **Phase 2: Cognitive Engine** - Implementation of persistent memory, real-time knowledge updates, and personalized responses.
- [x] **Phase 3: Tool Integration** - Expanding capabilities with external APIs (e.g., web search, weather forecasting).
- [ ] **Phase 4: Light Hardware Integration** - Integration with custom, modular IoT hardware (ESP32/Raspberry Pi) via local APIs/protocols to enable voice inquiries and lighting control.
- [ ] **Phase 5: Heavy Hardware Integration** - Communication layer to control external mechanical actuation systems (room's door and windows automation modules).

## Tech Stack (Current & Planned)
* **Core / Backend:** Python (Current)
* **Hardware Control:** C/C++ for precise and efficient microcontroller operation. (Planned)
* **Hardware & Fabrication:** Microcontrollers (ESP32, Arduino, Raspberry Pi), custom 3D-printed structures, and electronic actuators. (Planned)

## Changelog

* **`v0.1.0`** — *Tool Integration & In-Session Memory Update:*
  * Implemented context memory persistence within the active chat session.
  * Added web search integration via Tavily API and function calling schemas.
  * Integrated multi-tier exception handling for API and local runtime errors.

* **`v0.0.1`** — Initial Release: A functional, terminal-based voice chatbot programmed in Python, operating without persistent memory.