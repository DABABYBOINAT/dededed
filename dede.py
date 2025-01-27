# This challenge requires scripting skills to connect to the server, record the binary numbers involved, then solve the questions one-by-one. Remember to change the host and port variables at the bottom of the script.

import socket

bin_num_one = ""
bin_num_two = ""

operation = "default"

bit_shift_direction = ""
bit_shift_value = 1
bit_shift_target = 1

def bitwise_and(bin_num_one, bin_num_two):
  # convert binary strings to integers
  num1 = int(bin_num_one, 2)
  num2 = int(bin_num_two, 2)
  # perform the bitwise AND operation
  result = num1 & num2
  # convert the result back to binary string
  result_binary = bin(result)[2:] # remove '0b' prefix

  return result_binary

def bitwise_or(bin_num_one, bin_num_two):
  # convert binary strings to integers
  num1 = int(bin_num_one, 2)
  num2 = int(bin_num_two, 2)
  # perform the bitwise OR operation
  result = num1 | num2
  # convert the result back to binary string
  result_binary = bin(result)[2:] # remove '0b' prefix

  return result_binary

def bit_addition(bin_num_one, bin_num_two):
  num1 = int(bin_num_one, 2)
  num2 = int(bin_num_two, 2)
  # add the integers
  result = num1 + num2
  # convert the result back to binary
  result_binary = bin(result)[2:] # remove '0b' prefix

  return result_binary

def left_bit_shift(bit_shift_target):
  # convert binary string to integer
  target_int = None
  if bit_shift_target == 1:
    target_int = int(bin_num_one, 2)
  elif bit_shift_target == 2:
    target_int = int(bin_num_two, 2)
  # perform left shift
  shifted_int = target_int << bit_shift_value
  # convert back to binary string
  shifted_binary = bin(shifted_int)[2:]

  return shifted_binary

def right_bit_shift(bit_shift_target):
  # convert binary string to integer
  target_int = None
  if bit_shift_target == 1:
    target_int = int(bin_num_one, 2)
  elif bit_shift_target == 2:
    target_int = int(bin_num_two, 2)
  # perform left shift
  shifted_int = target_int >> bit_shift_value
  # convert back to binary string
  shifted_binary = bin(shifted_int)[2:]

  return shifted_binary

def binary_multiplication(bin_num_one, bin_num_two):
  # convert binary strings to integers
  num1 = int(bin_num_one, 2)
  num2 = int(bin_num_two, 2)
  # multiply the integers
  result = num1 * num2
  # conversaion back to binary
  result_binary = bin(result)[2:] # remove '0b' prefix

  return result_binary

def connect_to_server(host, port):
  global bin_num_one, bin_num_two, operation, bit_shift_target # declare global variables
  # create socket object
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    # connect to server
    client_socket.connect((host, port))
    print("Connected to server on port", port)

    # send data to server
    # client_socket.sendall(b'Hello, server!')

    # receive reply from server
    reply1 = client_socket.recv(1024)
    print("Reply from server:", reply1.decode())
    #scan the reply data line by line
    def check_content(replyNumber):
      global bin_num_one, bin_num_two, operation, bit_shift_target
      for line in replyNumber.decode().split('\n'):
        if "Binary Number 1:" in line:
          bin_num_one = line.split(":")[1].strip()
        elif "Binary Number 2:" in line:
          bin_num_two = line.split(":")[1].strip()
        elif "Operation" in line:
          operation = line.split("'")[1].strip()
        elif "shift of Binary Number 1" in line:
          bit_shift_target = 1
        elif "shift of Binary Number 2" in line:
          bit_shift_target = 2

    def send_answer():
      if str(operation) == ">>":
        data = right_bit_shift(bit_shift_target) + '\n'
        client_socket.sendall(data.encode())
      elif str(operation) == "<<":
        data = left_bit_shift(bit_shift_target) + '\n'
        client_socket.sendall(data.encode())
      elif str(operation) == "*":
        data = binary_multiplication(bin_num_one, bin_num_two) + '\n'
        client_socket.sendall(data.encode())
      elif str(operation) == "+":
        data = bit_addition(bin_num_one, bin_num_two) + '\n'
        client_socket.sendall(data.encode())
      elif str(operation) == "&":
        data = bitwise_and(bin_num_one, bin_num_two) + '\n'
        client_socket.sendall(data.encode())
      elif str(operation) == "|":
        data = bitwise_or(bin_num_one, bin_num_two) + '\n'
        client_socket.sendall(data.encode())

    check_content(reply1)
    send_answer()
    reply2 = client_socket.recv(1024)
    print("Reply from server:", reply2.decode())
    check_content(reply2)
    send_answer()
    reply3 = client_socket.recv(1024)
    print("Reply from server:", reply3.decode())
    check_content(reply3)
    send_answer()
    reply4 = client_socket.recv(1024)
    print("Reply from server:", reply4.decode())
    check_content(reply4)
    send_answer()
    reply5 = client_socket.recv(1024)
    print("Reply from server:", reply5.decode())
    check_content(reply5)
    send_answer()
    reply6 = client_socket.recv(1024)
    print("Reply from server:", reply6.decode())
    check_content(reply6)
    send_answer()
    reply7 = client_socket.recv(1024)
    print("Reply from server:", reply7.decode())
    if str(operation) == ">>":
      data = int(right_bit_shift(bit_shift_target), 2)
      hex_data = hex(data)[2:]
      data_final = hex_data + '\n'
      client_socket.sendall(data_final.encode())
    elif str(operation) == "<<":
      data = int(left_bit_shift(bit_shift_target), 2)
      hex_data = hex(data)[2:]
      data_final = hex_data + '\n'
      client_socket.sendall(data_final.encode())
    elif str(operation) == "*":
      data = int(binary_multiplication(bin_num_one, bin_num_two), 2)
      hex_data = hex(data)[2:]
      data_final = hex_data + '\n'
      client_socket.sendall(data_final.encode())
    elif str(operation) == "+":
      data = int(bit_addition(bin_num_one, bin_num_two), 2)
      hex_data = hex(data)[2:]
      data_final = hex_data + '\n'
      client_socket.sendall(data_final.encode())
    elif str(operation) == "&":
      data = int(bitwise_and(bin_num_one, bin_num_two), 2)
      hex_data = hex(data)[2:]
      data_final = hex_data + '\n'
      client_socket.sendall(data_final.encode())
    elif str(operation) == "|":
      data = int(bitwise_or(bin_num_one, bin_num_two), 2)
      hex_data = hex(data)[2:]
      data_final = hex_data + '\n'
      client_socket.sendall(data_final.encode())
    reply8 = client_socket.recv(1024)
    print("Reply from server:", reply8.decode())


  except Exception as e:
    print("Error:", e)

  finally:
    # close the socket
    client_socket.close()

if __name__ == "__main__":

  host = 'titan.picoctf.net'
  port = 56491

  # execute the main function
  connect_to_server(host, port)
