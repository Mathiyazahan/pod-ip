from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/get-pods-ip', methods=['GET'])
def get_pods_ip():
    # Get Pod names dynamically or specify them if known
    pod_names = ["my-app-pod-1", "my-app-pod-2"]  # Replace with your Pod names
    pod_ips = {}

    for pod_name in pod_names:
        try:
            ip = subprocess.check_output(
                ["kubectl", "get", "pod", pod_name, "-o", "jsonpath='{.status.podIP}'"]
            ).decode('utf-8').strip("'")
            pod_ips[pod_name] = ip
        except subprocess.CalledProcessError:
            pod_ips[pod_name] = "N/A"

    return jsonify(pod_ips)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
