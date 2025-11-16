def handle_choice(choice, builder):
    if choice == "1":
        builder.draw_dev_type()

    elif choice == "2":
        builder.draw_teams()

    elif choice == "3":
        builder.draw_themes()

    elif choice == "4":
        builder.draw_technologies()

    elif choice == "5":
        (builder.draw_dev_type()
                .draw_teams()
                .draw_themes()
                .draw_technologies())

    else:
        print("Opção inválida.")
