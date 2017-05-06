_NEW_STUD_OF_GROUP = ("Votre compte OLA a été créé !", "Bonjour,<br/><p>Votre compte vient d'être créé dans l'Outil du "
                                                       "Livret de l'Alternant dans le groupe <b>#GROUPE</b>. Vous pouvez dès "
                                                       "maintenant l'activer, puis créer un livret en vous rendant à l'adresse : <br/>"
                                                       "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_STUD_OF_GROUP = (
    "Vous avez été ajouté à un groupe OLA !", "Bonjour,<br/><p>Votre compte vient d'être ajouté dans l'Outil du "
                                              "Livret de l'Alternant au groupe <b>#GROUPE</b>. Vous pouvez dès "
                                              "maintenant créer un livret en vous rendant à l'adresse : <br/>"
                                              "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_NEW_RESP_OF_GROUP = ("Votre compte OLA a été créé !", "Bonjour,<br/><p>Votre compte vient d'être créé dans l'Outil du "
                                                       "Livret de l'Alternant en tant que responsable du groupe <b>#GROUPE</b>. Vous pouvez dès "
                                                       "maintenant l'activer en vous rendant à l'adresse : <br/>"
                                                       "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_RESP_OF_GROUP = (
    "Vous avez été ajouté à un groupe OLA !", "Bonjour,<br/><p>Votre compte vient d'être ajouté dans l'Outil du "
                                              "Livret de l'Alternant en tant que responsable du groupe <b>#GROUPE</b>. Vous pouvez dès "
                                              "maintenant y accéder en vous rendant à l'adresse : <br/>"
                                              "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_NEW_SEC_OF_GROUP = ("Votre compte OLA a été créé !", "Bonjour,<br/><p>Votre compte vient d'être créé dans l'Outil du "
                                                      "Livret de l'Alternant en tant que secrétaire du groupe <b>#GROUPE</b>. Vous pouvez dès "
                                                      "maintenant l'activer en vous rendant à l'adresse : <br/>"
                                                      "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_SEC_OF_GROUP = (
    "Vous avez été ajouté à un groupe OLA !", "Bonjour,<br/><p>Votre compte vient d'être ajouté dans l'Outil du "
                                              "Livret de l'Alternant en tant que secrétaire du groupe <b>#GROUPE</b>. Vous pouvez dès "
                                              "maintenant y accéder en vous rendant à l'adresse : <br/>"
                                              "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_NEW_ETUTOR_ADDED = ("Votre compte OLA a été créé !", "Bonjour,<br/><p>Votre compte vient d'être créé dans l'Outil du "
                                                      "Livret de l'Alternant de l'Université Toulouse Jean-Jaurès en tant que tuteur dans le groupe <b>#GROUPE</b>. Vous pouvez dès "
                                                      "maintenant l'activer en vous rendant à l'adresse : <br/>"
                                                      "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")

_ETUTOR_ADDED = (
    "Vous avez été déclaré comme tuteur dans OLA !", "Bonjour,<br/><p>Votre compte vient d'être ajouté dans l'Outil du "
                                                     "Livret de l'Alternant de l'Université Toulouse Jean-Jaurès en tant que tuteur dans le groupe <b>#GROUPE</b>. Vous pouvez dès "
                                                     "maintenant accéder à votre compte en vous rendant à l'adresse : <br/>"
                                                     "<a href='#URL'>#URL</a></p><p>Bonne journée !</p>")


def getMailContent(mail_type, args):
    if mail_type == "NEW_STUD_OF_GROUP":
        mail = _NEW_STUD_OF_GROUP
    elif mail_type == "STUD_OF_GROUP":
        mail = _STUD_OF_GROUP
    elif mail_type == "NEW_RESP_OF_GROUP":
        mail = _NEW_RESP_OF_GROUP
    elif mail_type == "RESP_OF_GROUP":
        mail = _RESP_OF_GROUP
    elif mail_type == "NEW_SEC_OF_GROUP":
        mail = _NEW_SEC_OF_GROUP
    elif mail_type == "SEC_OF_GROUP":
        mail = _SEC_OF_GROUP
    elif mail_type == "NEW_ETUTOR_ADDED":
        mail = _NEW_ETUTOR_ADDED
    elif mail_type == "ETUTOR_ADDED":
        mail = _ETUTOR_ADDED
    else:
        raise Exception("Unknown mail type !")

    obj = mail[0]
    content = str(mail[1])
    for key, value in args.items():
        content = content.replace("#" + key, value)
    return (obj, content)
