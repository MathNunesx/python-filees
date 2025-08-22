# Tupla contendo os contatos suportados pelo sistema

contato_sup = ("telefone", "email", "endereco")

agenda = {
    "Pessoa 1": {
        "telefone": ["11 1234-5678"],
        "email": ["pessoa@gmail.com", "email@trabalho.com"],
        "endereco":["Rua 345"]
    },

    "Pessoa 2": {
        "telefone": ["11 12787-5678"],
        "email": ["pessoa2@gmail.com", "email2@trabalho.com"],
        "endereco":["Rua 378"]
    }
}

def contato_for_text(contact_name:str, **contact_metods):
    text_format = f"{contact_name}"
    for meio_contact, contato in contact_metods.items():
        text_format = f"{text_format}\n{meio_contact.upper()}"
        contador = 1
        for valor in contato:
            text_format = f"{text_format}\n\t{contador} - {valor.upper()}"
            contact_metods = contador + 1 

    return text_format

# print(contato_for_text("Pessoa 2", **agenda["Pessoa 2"]))

def agenda_for_text(**agenda_completa):
    text_format = ""
    for contact_name, contact_metods in agenda_completa.items():
        text_format = f"{text_format}{contato_for_text(contact_name, **contact_metods)}\n"
        text_format = f"{text_format}-----------------------------------------\n"
    return text_format


print(agenda_for_text(**agenda))

def name_contact_change(agenda_original:dict, original_name:str, update_name:str):
    if original_name in agenda_original.keys():
        contacts_copy = agenda_original[original_name].copy()
        agenda_original.pop(original_name)
        agenda_original[update_name] = contacts_copy
        return True
    return False

name_contact_change(agenda, "Pessoa 2", "Super Pessoa")
print(agenda_for_text(**agenda))

def contact_metod_change(contact_list: list, old_valor:str, new_valor:str):
    if old_valor in contact_list:
        old_valor_position = contact_list.index(old_valor)
        contact_list.pop(old_valor_position)
        contact_list.insert(old_valor_position, new_valor)
        return True
    return False

contact_metod_change(agenda["Pessoa 1"]["telefone"], "11 1234-5678","123")
print(agenda_for_text(**agenda))

def contact_delete(agenda:dict, contact_name:str):
    if contact_name in agenda.keys():
        agenda.pop(contact_name)
        return True
    return False

contact_delete(agenda, "Pessoa 1")
print(agenda_for_text(**agenda))

def add_contact(agenda:dict, contact_name:str, **contact_metods):
    agenda[contact_name] =  contact_metods

add_contact(agenda, "Riveraldo", telefone=["114082"], email=["river@email.com"])
print(agenda_for_text(**agenda))


def add_contact_metods(contact_metods:dict, include_metod:str, include_valor:str):
    if include_metod in contact_metods.keys():
        contact_metods[include_metod].append(include_valor)
        return True
    elif include_metod in contato_sup:
        contact_metods[include_metod] = [include_valor]
        return True
    return False

add_contact_metods(agenda["Riveraldo"], "endereco", "Rua Blue River")
print(agenda_for_text(**agenda))


def show_menu():
    print("\n\n")
    print("1 - Incluir contato na agenda")
    print("2 - Incluir uma forma de contato")
    print("3 - Alterar o nome do contato")
    print("4 - Alterar uma forma de contato")
    print("5 - Exibir um contato")
    print("6 - Exibir toda a agenda")
    print("7 - Excluir contato")
    print("8 - Sair")
    print("\n\n")

