#!/usr/bin/env python3

import os, sys

current_working_directory = os.curdir
rooms_file_path = os.path.join(os.curdir, "quartos.txt")
bookings_file_path = os.path.join(os.curdir, "reservas.txt")

try:
    rooms_file = open(rooms_file_path)
    with open(rooms_file_path) as rooms_file:
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("| Número do quarto |    Descrição   | Valor da diária |")
        for line in rooms_file:
            room_number, room_description, room_booking_price = line.split(",")
            room_booking_price = float(room_booking_price)
            print("|-----------------------------------------------------|")
            print(
                f"| {room_number:>16} | "
                f"{room_description:^14} | "
                f"{room_booking_price:>15,.2f} |"
            )
        print("|_____________________________________________________|")

    print("\nVamos fazer sua reserva. Para isso, precisamos de alguns dados.")
    hotel_guest_name = input("Qual é o seu nome?\n").strip()
    selected_room_number = input("Qual é o número do quarto?\n").strip()
    booking_period_in_days = input(
        "Por quantos dias deseja reservar o quarto?\n"
    ).strip()

    # TODO: Tratar a exceção na leitura do arquivo de reservas
    booked_rooms = []
    with open(bookings_file_path, "a+") as bookings_file:
        bookings_file.seek(0)
        for line in bookings_file:
            _hotel_guest, room_number, *_ = line.split(",")
            booked_rooms.append(room_number.strip())

        if selected_room_number in booked_rooms:
            print(
                "\nEste quarto já está reservado. "
                "Por favor, tente reservar outro quarto. 🪃"
            )
        else:
            bookings_file.write(
                f"{hotel_guest_name},"
                f"{selected_room_number},"
                f"{booking_period_in_days}\n"
            )
            print("\nReserva concluída com sucesso! 🎉")
except ValueError:
    print(
        "A leitura do arquivo de reservas não pôde concluir "
        "a análise dos dados. Por favor, entre em contato com o suporte. 📨"
    )
    sys.exit(1)
except FileNotFoundError:
    print(
        "Não foi possível abrir o arquivos que contém os dados "
        "dos quartos disponíveis para reserva. ⛔"
    )
    sys.exit(1)
