# 🖥️ RPi5 OLED Monitor - Home Assistant Add-on

[![Home Assistant][ha-shield]][ha-url]
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

Display system information on an I2C OLED screen connected to your Raspberry Pi 5 running Home Assistant OS.

![RPi5 OLED Monitor](https://via.placeholder.com/600x200/1e88e5/ffffff?text=RPi5+OLED+Monitor)

## ✨ Features

- 📊 Real-time CPU usage and frequency monitoring
- 💾 RAM usage statistics
- 🌡️ System temperature monitoring
- 💽 Storage space tracking
- 🌐 Network IP address display
- 🔄 Auto-refresh every few seconds

## 📋 Requirements

- Raspberry Pi 5 with Home Assistant OS
- I2C OLED Display (address 0x2D)
- I2C enabled on your system

## 🚀 Installation

### Step 1: Enable I2C

**This is mandatory before installing the addon!**

1. Go to **Supervisor → Add-on Store → Menu (⋮) → Repositories**
2. Add repository: `https://github.com/Poeschl/Hassio-Addons`
3. Install and start **"HassOS I2C Configurator"**
4. **Perform a complete shutdown twice** (unplug power physically)
5. Verify I2C is active: `ls /dev/i2c-0`

### Step 2: Install the Add-on

1. Go to **Supervisor → Add-on Store → Menu (⋮) → Repositories**
2. Add this repository:
`https://github.com/davidelolli/homeassistant-rpi5-oled`
3. Find **"RPi5 OLED Monitor"** in the add-on list
4. Click **"Install"**
5. Click **"Start"**

## 📖 Documentation

For detailed documentation, troubleshooting, and configuration options, see [DOCS.md](rpi5_oled/DOCS.md).

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please open an [issue](https://github.com/davidelolli/homeassistant-rpi5-oled/issues).

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 👨‍💻 Author

Developed by **Davide Lolli** for the Home Assistant community.

---

**⭐ If this add-on helps you, consider giving it a star on GitHub!**

[ha-shield]: https://img.shields.io/badge/Home%20Assistant-Add--on-blue.svg
[ha-url]: https://www.home-assistant.io/
[releases-shield]: https://img.shields.io/github/v/release/davidelolli/homeassistant-rpi5-oled
[releases]: https://github.com/TUO_USERNAME/homeassistant-rpi5-oled/releases
[license-shield]: https://img.shields.io/github/license/davidelolli/homeassistant-rpi5-oled
