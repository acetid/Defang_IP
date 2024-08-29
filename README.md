# Defang_IP

# IP Address Formatter

This Python script takes an IP address as input and formats it by replacing the periods (`.`) with `[.]`. This can be useful for obfuscating IP addresses in text or for specific formatting requirements.

## How It Works

**Function**: 
   - The script defines a function `ip_address()` that:
     - Takes an IP address as a string input.
     - Splits the IP address into segments based on the periods.
     - Rejoins the segments using `[.]` as the separator.
     - Returns the newly formatted IP address.

# Usage

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

2. **Create or Edit the Script**:
- Save the script provided above as ip_formatter.py in the cloned repository or modify the existing file.

3. **Run the script**:
```
python3 ip_formatter.py
```

4. **Input Your IP Address**:
- Edit the line my_new_ip = ip_address("192.168.1.1") in the script to use the IP address you want to format.

5. **View the Output**:
- The script will print the formatted IP address with [.] replacing each ..

# Requirements

- Python 3
