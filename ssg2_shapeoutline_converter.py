import base64
import struct
import json

def vertices_to_base64(vertices):
    binary_data = b''.join(struct.pack('ff', *vertex) for vertex in vertices)
    base64_string = base64.b64encode(binary_data).decode('utf-8')
    return base64_string

def base64_to_vertices(base64_string):
    binary_data = base64.b64decode(base64_string)
    vertex_count = len(binary_data) // 8  # 8 bytes per vertex (2 floats of 4 bytes each)
    vertices = []

    for i in range(vertex_count):
        chunk = binary_data[i * 8:(i + 1) * 8]
        x, y = struct.unpack('ff', chunk)  # 'ff' format string for two floats
        vertices.append((x, y))

    return vertices

def main():
    while True:
        print("\nChoose mode:")
        print("1: Convert JSON to Base64")
        print("2: Convert Base64 to JSON")
        print("3: Exit")

        mode = input("Enter mode (1, 2, or 3): ").strip()

        if mode == '1':
            print("Paste JSON (e.g., [[0.5, 0.5], [0.0, 0.0], [1.0, 1.0]]):")
            json_input = input().strip()
            try:
                vertices = json.loads(json_input)
                base64_string = vertices_to_base64(vertices)
                print("Base64 Output:")
                print(base64_string)
            except json.JSONDecodeError:
                print("Invalid JSON input. Please try again.")
        elif mode == '2':
            print("Paste Base64 string:")
            base64_input = input().strip()
            try:
                vertices = base64_to_vertices(base64_input)
                json_output = json.dumps(vertices, indent=4)
                print("JSON Output:")
                print(json_output)
            except (base64.binascii.Error, struct.error):
                print("Invalid Base64 input. Please try again.")
        elif mode == '3':
            print("Exiting the script.")
            break
        else:
            print("Invalid mode. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()