# To use this script, ensure you have installed the speedtest-cli package:
# Run the following command in your terminal:
# pip install speedtest-cli

import speedtest

# Create a Speedtest object
st = speedtest.Speedtest()

# Get best server based on ping
best_server = st.get_best_server()

# Perform download and upload speed tests
download_speed = st.download() / 1_000_000  # Convert from bits to Mbps
upload_speed = st.upload() / 1_000_000      # Convert from bits to Mbps
ping = st.results.ping

# Print results
print(f"Best Server:     {best_server['host']} ({best_server['name']}, {best_server['country']})")
print(f"Server IP:       {best_server['ip']}")
print(f"Download Speed:  {download_speed:.2f} Mbps")
print(f"Upload Speed:    {upload_speed:.2f} Mbps")
print(f"Ping:            {ping:.2f} ms")
# Print the full results