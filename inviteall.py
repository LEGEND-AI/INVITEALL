import asyncio
import os
import sys
from datetime import datetime

import telethon.utils
from telethon import TelegramClient, events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.tl import functions
from telethon.tl.functions.channels import (
    GetFullChannelRequest,
    InviteToChannelRequest,
    LeaveChannelRequest,
)
from telethon.tl.functions.messages import GetFullChatRequest

from Config import (
    API_H,
    API_H2,
    API_H3,
    API_H4,
    API_H5,
    API_H6,
    API_H7,
    API_H8,
    API_H9,
    API_H10,
    API_H11,
    API_H12,
    API_H13,
    API_H14,
    API_H15,
    API_H16,
    API_H17,
    API_H18,
    API_H19,
    API_H20,
    API_H21,
    API_H22,
    API_H23,
    API_H24,
    API_H25,
    API_ID,
    API_ID2,
    API_ID3,
    API_ID4,
    API_ID5,
    API_ID6,
    API_ID7,
    API_ID8,
    API_ID9,
    API_ID10,
    API_ID11,
    API_ID12,
    API_ID13,
    API_ID14,
    API_ID15,
    API_ID16,
    API_ID17,
    API_ID18,
    API_ID19,
    API_ID20,
    API_ID21,
    API_ID22,
    API_ID23,
    API_ID24,
    API_ID25,
    GROUP_USERNAME,
    STRING,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING6,
    STRING7,
    STRING8,
    STRING9,
    STRING10,
    STRING11,
    STRING12,
    STRING13,
    STRING14,
    STRING15,
    STRING16,
    STRING17,
    STRING18,
    STRING19,
    STRING20,
    STRING21,
    STRING22,
    STRING23,
    STRING24,
    STRING25,
    SUDO,
)

grp = GROUP_USERNAME

if "@" in grp:
    grp = grp.replace("@", "")

sup = API_ID
aa = API_ID2 or sup
ba = API_ID3 or sup
ca = API_ID4 or sup
da = API_ID5 or sup
ea = API_ID6 or sup
fa = API_ID7 or sup
ga = API_ID8 or sup
ha = API_ID9 or sup
ia = API_ID10 or sup
ja = API_ID11 or sup
ka = API_ID12 or sup
la = API_ID13 or sup
ma = API_ID14 or sup
na = API_ID15 or sup
oa = API_ID16 or sup
pa = API_ID17 or sup
qa = API_ID18 or sup
ra = API_ID19 or sup
sa = API_ID20 or sup
ta = API_ID21 or sup
ua = API_ID22 or sup
va = API_ID23 or sup
wa = API_ID24 or sup
xa = API_ID25 or sup

sap = API_H
ab = API_H2 or sap
bb = API_H3 or sap
cb = API_H4 or sap
db = API_H5 or sap
eb = API_H6 or sap
fb = API_H7 or sap
gb = API_H8 or sap
hb = API_H9 or sap
ib = API_H10 or sap
jb = API_H11 or sap
kb = API_H12 or sap
lb = API_H13 or sap
mb = API_H14 or sap
nb = API_H15 or sap
ob = API_H16 or sap
pb = API_H17 or sap
qb = API_H18 or sap
rb = API_H19 or sap
sb = API_H20 or sap
tb = API_H21 or sap
ub = API_H22 or sap
vb = API_H23 or sap
wb = API_H24 or sap
xb = API_H25 or sap

smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)


async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put

    if smex:
        session_name = StringSession(str(smex))
        print("String 1 Found")
        idk = TelegramClient(
            session=session_name,
            api_id=sup,
            api_hash=sap,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # idk = TelegramClient(session_name, sup, sap)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await idk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await idk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, sup, sap)
        try:
            await idk.start()
        except Exception:
            pass

    if smexx:
        session_name = StringSession(str(smexx))
        print("String 2 Found")
        ydk = TelegramClient(
            session=session_name,
            api_id=aa,
            api_hash=ab,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await ydk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await ydk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 2 not Found")
        session_name = "startup"
        ydk = TelegramClient(session_name, aa, ab)
        try:
            await ydk.start()
        except Exception:
            pass

    if smexxx:
        session_name = StringSession(str(smexxx))
        print("String 3 Found")
        wdk = TelegramClient(
            session=session_name,
            api_id=ba,
            api_hash=bb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # wdk = TelegramClient(StringSession(session_name), ba, bb)
        try:
            print("Booting Up The Client 3")
            await wdk.start()
            await wdk(
                functions.channels.JoinChannelRequest(channel="@Legend_k_Userbot")
            )
            await wdk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await wdk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 3 not Found")
        session_name = "startup"
        wdk = TelegramClient(
            session=session_name,
            api_id=ba,
            api_hash=bb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # wdk = TelegramClient(session_name, ba, bb)
        try:
            await wdk.start()
        except Exception:
            pass

    if smexxxx:
        session_name = StringSession(str(smexxxx))
        print("String 4 Found")
        hdk = TelegramClient(
            session=session_name,
            api_id=ca,
            api_hash=cb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # hdk = TelegramClient(StringSession(session_name), ca, cb)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await hdk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await hdk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 4 not Found")
        session_name = "startup"
        hdk = TelegramClient(
            session=session_name,
            api_id=ca,
            api_hash=cb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # hdk = TelegramClient(session_name, ca, cb)
        try:
            await hdk.start()
        except Exception:
            pass

    if smexxxxx:
        session_name = StringSession(str(smexxxxx))
        print("String 5 Found")
        sdk = TelegramClient(
            session=session_name,
            api_id=da,
            api_hash=db,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # sdk = TelegramClient(StringSession(session_name), da, db)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await sdk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await sdk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 5 not Found")
        session_name = "startup"
        sdk = TelegramClient(
            session=session_name,
            api_id=da,
            api_hash=db,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # sdk = TelegramClient(session_name, da, db)
        try:
            await sdk.start()
        except Exception:
            pass

    if sixth:
        session_name = StringSession(str(sixth))
        print("String 6 Found")
        adk = TelegramClient(
            session=session_name,
            api_id=ea,
            api_hash=eb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # adk = TelegramClient(StringSession(session_name), ea, eb)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await adk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            await adk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 6 not Found")
        session_name = "startup"
        adk = TelegramClient(
            session=session_name,
            api_id=ea,
            api_hash=eb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # adk = TelegramClient(session_name, ea, eb)
        try:
            await adk.start()
        except Exception:
            pass

    if seven:
        session_name = StringSession(str(seven))
        print("String 7 Found")
        bdk = TelegramClient(
            session=session_name,
            api_id=fa,
            api_hash=fb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # bdk = TelegramClient(StringSession(session_name), fa, fb)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await bdk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await bdk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 7 not Found")
        session_name = "startup"
        bdk = TelegramClient(
            session=session_name,
            api_id=fa,
            api_hash=fb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # bdk = TelegramClient(session_name, fa, fb)
        try:
            await bdk.start()
        except Exception:
            pass

    if eight:
        session_name = StringSession(str(eight))
        print("String 8 Found")
        cdk = TelegramClient(
            session=session_name,
            api_id=ga,
            api_hash=gb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # cdk = TelegramClient(StringSession(session_name), ga, gb)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await cdk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await cdk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 8 not Found")
        session_name = "startup"
        cdk = TelegramClient(session_name, ga, gb)
        try:
            await cdk.start()
        except Exception:
            pass

    if ninth:
        session_name = StringSession(str(ninth))
        print("String 9 Found")
        ddk = TelegramClient(
            session=session_name,
            api_id=ha,
            api_hash=hb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # ddk = TelegramClient(StringSession(session_name), ha, hb)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await ddk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await ddk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 9 not Found")
        session_name = "startup"
        ddk = TelegramClient(session_name, ha, hb)
        try:
            await ddk.start()
        except Exception:
            pass

    if tenth:
        session_name = StringSession(str(tenth))
        print("String 10 Found")
        edk = TelegramClient(
            session=session_name,
            api_id=ia,
            api_hash=ib,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # edk = TelegramClient(StringSession(session_name), ia, ib)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await edk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await edk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 10 not Found")
        session_name = "startup"
        edk = TelegramClient(session_name, ia, ib)
        try:
            await edk.start()
        except Exception:
            pass

    if eleve:
        session_name = StringSession(str(eleve))
        print("String 11 Found")
        vkk = TelegramClient(
            session=session_name,
            api_id=ja,
            api_hash=jb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # vkk = TelegramClient(StringSession(session_name), ja, jb)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await vkk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            await vkk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 11 not Found")
        session_name = "startup"
        vkk = TelegramClient(session_name, ja, jb)
        try:
            await vkk.start()
        except Exception:
            pass

    if twelv:
        session_name = StringSession(str(twelv))
        kkk = TelegramClient(
            session=session_name,
            api_id=ka,
            api_hash=kb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # kkk = TelegramClient(StringSession(session_name), ka, kb)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await kkk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await kkk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 12 not Found")
        session_name = "startup"
        kkk = TelegramClient(session_name, ka, kb)
        try:
            await kkk.start()
        except Exception:
            pass

    if thirt:
        session_name = StringSession(str(thirt))
        print("String 13  Found")
        lkk = TelegramClient(
            session=session_name,
            api_id=la,
            api_hash=lb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # lkk = TelegramClient(StringSession(session_name), la, lb)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await lkk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await lkk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 13 not Found")
        session_name = "startup"
        lkk = TelegramClient(session_name, la, lb)
        try:
            await lkk.start()
        except Exception:
            pass

    if forte:
        session_name = StringSession(str(forte))
        print("String 14 Found")
        mkk = TelegramClient(
            session=session_name,
            api_id=ma,
            api_hash=mb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # mkk = TelegramClient(StringSession(session_name), ma, mb)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await mkk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await mkk(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 14 not Found")
        session_name = "startup"
        mkk = TelegramClient(session_name, ma, mb)
        try:
            await mkk.start()
        except Exception:
            pass

    if fifth:
        session_name = StringSession(str(fifth))
        print("String 15 Found")
        sid = TelegramClient(
            session=session_name,
            api_id=na,
            api_hash=nb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # sid = TelegramClient(StringSession(session_name), na, nb)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await sid(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await sid(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 15 not Found")
        session_name = "startup"
        sid = TelegramClient(session_name, na, nb)
        try:
            await sid.start()
        except Exception:
            pass

    if sieee:
        session_name = StringSession(str(sieee))
        print("String 16 Found")
        shy = TelegramClient(
            session=session_name,
            api_id=oa,
            api_hash=ob,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # shy = TelegramClient(StringSession(session_name), oa, ob)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await shy(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await shy(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, oa, ob)
        try:
            await shy.start()
        except Exception:
            pass

    if seeee:
        session_name = StringSession(str(seeee))
        print("String 17 Found")
        aan = TelegramClient(
            session=session_name,
            api_id=pa,
            api_hash=pb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # aan = TelegramClient(StringSession(session_name), pa, pb)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await aan(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await aan(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, pa, pb)
        try:
            await aan.start()
        except Exception:
            pass

    if eieee:
        session_name = StringSession(str(eieee))
        print("String 18 Found")
        ake = TelegramClient(
            session=session_name,
            api_id=qa,
            api_hash=qb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # ake = TelegramClient(StringSession(session_name), qa, qb)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await ake(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await ake(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, qa, qb)
        try:
            await ake.start()
        except Exception:
            pass

    if nieee:
        session_name = StringSession(str(nieee))
        print("String 19 Found")
        eel = TelegramClient(
            session=session_name,
            api_id=ra,
            api_hash=rb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # eel = TelegramClient(StringSession(session_name), ra, rb)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await eel(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await eel(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, ra, rb)
        try:
            await idk.start()
        except Exception:
            pass

    if gandu:
        session_name = StringSession(str(gandu))
        print("String 20 Found")
        khu = TelegramClient(
            session=session_name,
            api_id=sa,
            api_hash=sb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # khu = TelegramClient(StringSession(session_name), sa, sb)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await khu(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await khu(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, sa, sb)
        try:
            await khu.start()
        except Exception:
            pass

    if ekish:
        session_name = StringSession(str(ekish))
        print("String 21 Found")
        shi = TelegramClient(
            session=session_name,
            api_id=ta,
            api_hash=tb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # shi = TelegramClient(StringSession(session_name), ta, tb)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await shi(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await shi(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, ta, tb)
        try:
            await shi.start()
        except Exception:
            pass

    if baish:
        session_name = StringSession(str(baish))
        print("String 22 Found")
        yaa = TelegramClient(
            session=session_name,
            api_id=ua,
            api_hash=ub,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # yaa = TelegramClient(StringSession(session_name), ua, ub)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await yaa(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await yaa(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, ua, ub)
        try:
            await yaa.start()
        except Exception:
            pass

    if teish:
        session_name = StringSession(str(teish))
        print("String 23 Found")
        dav = TelegramClient(
            session=session_name,
            api_id=va,
            api_hash=vb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # dav = TelegramClient(StringSession(session_name), va, vb)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await dav(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await dav(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, va, vb)
        try:
            await dav.start()
        except Exception:
            pass

    if tfour:
        session_name = StringSession(str(tfour))
        print("String 24 Found")
        raj = TelegramClient(
            session=session_name,
            api_id=wa,
            api_hash=wb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # raj = TelegramClient(StringSession(session_name), wa, wb)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await raj(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await raj(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, wa, wb)
        try:
            await raj.start()
        except Exception:
            pass

    if tfive:
        session_name = StringSession(str(tfive))
        print("String 25 Found")
        put = TelegramClient(
            session=session_name,
            api_id=xa,
            api_hash=xb,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        # put = TelegramClient(StringSession(session_name), xa, xb)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(
                functions.channels.JoinChannelRequest(channel="@Legend_K_Userbot")
            )
            await put(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            await put(
                functions.channels.JoinChannelRequest(channel="@Official_K_LegendBot ")
            )
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, xa, xb)
        try:
            await put.start()
        except Exception:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


async def get_chatinfo(event):
    yukki = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    chat = yukki[0]
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.edit(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝐉𝐎𝐢𝐍 𝐇𝐎𝐆𝐘𝐀 𝐕𝐀𝐈 AB BATA KISKO MARU PAHLE🔥")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝐉𝐎𝐢𝐍 𝐇𝐎𝐆𝐘𝐀 𝐕𝐀𝐈 𝐀𝐁 𝐁𝐓𝐀 𝐊𝐈𝐒𝐊𝐈 𝐌𝐀𝐑𝐔😏🔥")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if yukki:
            bc = yukki[0]
            bc = int(bc)
            text = "BOT Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))
    else:
        await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"PING PONG!\n`{ms}` 𝗺𝘀")


@idk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.limit"))
async def _(event):
    if event.sender_id in SMEX_USERS:
        bot = "@SpamBot"
        async with event.client.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                yup = await conv.get_response()
                await event.reply(yup.text)
            except YouBlockedUserError:
                await event.client(functions.contacts.UnblockRequest("@spambot"))
                await event.reply(
                    "Done @spambot Unblocked and Now Again Type .limit!",
                    parse_mode=None,
                    link_preview=None,
                )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await idk.send_message(
            e.chat_id, f"Hello Sir\nMy Inviteall Command Handler ~ .\nI am client 1"
        )


@ydk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await ydk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ *\nI am client 2"
        )


@wdk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await wdk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ?\nI am client 3"
        )


@hdk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await hdk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ +\nI am client 4"
        )


@sdk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await sdk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ -\nI am client 5"
        )


@adk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await adk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ×\nI am client 6"
        )


@bdk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await bdk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ÷\nI am client 7"
        )


@cdk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await cdk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ =\nI am client 8"
        )


@edk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await edk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ .\nI am client 9"
        )


@ddk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await ddk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ *\nI am client 10"
        )


@vkk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await vkk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ?\nI am client 11"
        )


@kkk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await kkk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ +\nI am client 12"
        )


@lkk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await lkk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ -\nI am client 13"
        )


@mkk.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await mkk.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ×\nI am client 14"
        )


@sid.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await sid.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ÷\nI am client 15"
        )


@shy.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await shy.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ =\nI am client 16"
        )


@aan.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await aan.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ .\nI am client 17"
        )


@ake.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await ake.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ *\nI am client 18"
        )


@eel.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await eel.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ?\nI am client 19"
        )


@khu.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await khu.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ +\nI am client 20"
        )


@shi.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await shi.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ -\nI am client 21"
        )


@yaa.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await yaa.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ×\nI am client 22"
        )


@dav.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await dav.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ ÷\nI am client 23"
        )


@raj.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await raj.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ =\nI am client 24"
        )


@put.on(events.NewMessage(incoming=True, pattern=r"\.cmd"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        await put.send_message(
            e.chat_id, "Hello Sir\nMy Inviteall Command Handler ~ .\nI am client 25"
        )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for x in event.client.iter_participants(
            legend.full_chat.id, aggressive=True
        ):
            try:
                await idk(InviteToChannelRequest(channel=chat, users=[x.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@ydk.on(events.NewMessage(incoming=True, pattern=r"\*inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        yukki = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await ydk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@wdk.on(events.NewMessage(incoming=True, pattern=r"\?inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await wdk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@hdk.on(events.NewMessage(incoming=True, pattern=r"\+inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await hdk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@sdk.on(events.NewMessage(incoming=True, pattern=r"\-inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await sdk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@adk.on(events.NewMessage(incoming=True, pattern=r"\×inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await adk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@bdk.on(events.NewMessage(incoming=True, pattern=r"\÷inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await bdk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@cdk.on(events.NewMessage(incoming=True, pattern=r"\=inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await cdk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await edk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@ddk.on(events.NewMessage(incoming=True, pattern=r"\*inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await ddk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@vkk.on(events.NewMessage(incoming=True, pattern=r"\?inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await vkk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@kkk.on(events.NewMessage(incoming=True, pattern=r"\+inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await kkk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@lkk.on(events.NewMessage(incoming=True, pattern=r"\-inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await lkk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@mkk.on(events.NewMessage(incoming=True, pattern=r"\×inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await mkk(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@sid.on(events.NewMessage(incoming=True, pattern=r"\÷inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await sid(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@shy.on(events.NewMessage(incoming=True, pattern=r"\=inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await shy(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@aan.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await aan(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@ake.on(events.NewMessage(incoming=True, pattern=r"\*inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await ake(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@eel.on(events.NewMessage(incoming=True, pattern=r"\?inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await eel(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@khu.on(events.NewMessage(incoming=True, pattern=r"\+inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await khu(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@shi.on(events.NewMessage(incoming=True, pattern=r"\-inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await shi(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@yaa.on(events.NewMessage(incoming=True, pattern=r"\×inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await yaa(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@dav.on(events.NewMessage(incoming=True, pattern=r"\÷inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await dav(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@raj.on(events.NewMessage(incoming=True, pattern=r"\=inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        yukki = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for x in event.client.iter_participants(
            legend.full_chat.id, aggressive=True
        ):
            try:
                await raj(InviteToChannelRequest(channel=event.chat_id, users=[x.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@put.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS:
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        else:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None)
        legend = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"

        await krishna.edit(
            "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_K_Userbot)**\n\n`🔸Inviting Users.......`"
        )
        async for user in event.client.iter_participants(legend.full_chat.id):
            try:
                await put(InviteToChannelRequest(channel=chat, users=[user.id]))
                s = s + 1
                await krishna.edit(
                    f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
                )
            except Exception as e:
                error = str(e)
                f = f + 1
        return await krishna.edit(
            f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_K_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
        )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await idk.disconnect()
        except Exception:
            pass
        try:
            await ydk.disconnect()
        except Exception:
            pass
        try:
            await wdk.disconnect()
        except Exception:
            pass
        try:
            await hdk.disconnect()
        except Exception:
            pass
        try:
            await sdk.disconnect()
        except Exception:
            pass
        try:
            await adk.disconnect()
        except Exception:
            pass
        try:
            await bdk.disconnect()
        except Exception:
            pass
        try:
            await cdk.disconnect()
        except Exception:
            pass
        try:
            await ddk.disconnect()
        except Exception:
            pass
        try:
            await edk.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


text = """
CONGRATS 🥳🥳🥳 & SAY THANKS TO LEGENDBOY (LegendBoy_XD)
"""

print(text)
print("")
print("🙏🔥🔥 BOT STARTED SUCCESFULLY.🔥🔥🙏")


if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception:
        pass
    try:
        ydk.disconnect()
    except Exception:
        pass
    try:
        wdk.disconnect()
    except Exception:
        pass
    try:
        hdk.disconnect()
    except Exception:
        pass
    try:
        sdk.disconnect()
    except Exception:
        pass
    try:
        adk.disconnect()
    except Exception:
        pass
    try:
        bdk.disconnect()
    except Exception:
        pass
    try:
        cdk.disconnect()
    except Exception:
        pass
    try:
        edk.disconnect()
    except Exception:
        pass
    try:
        ddk.disconnect()
    except Exception:
        pass
    try:
        vkk.disconnect()
    except Exception:
        pass
    try:
        kkk.disconnect()
    except Exception:
        pass
    try:
        lkk.disconnect()
    except Exception:
        pass
    try:
        mkk.disconnect()
    except Exception:
        pass
    try:
        sid.disconnect()
    except Exception:
        pass
    try:
        shy.disconnect()
    except Exception:
        pass
    try:
        aan.disconnect()
    except Exception:
        pass
    try:
        ake.disconnect()
    except Exception:
        pass
    try:
        eel.disconnect()
    except Exception:
        pass
    try:
        khu.disconnect()
    except Exception:
        pass
    try:
        shi.disconnect()
    except Exception:
        pass
    try:
        yaa.disconnect()
    except Exception:
        pass
    try:
        dav.disconnect()
    except Exception:
        pass
    try:
        raj.disconnect()
    except Exception:
        pass
    try:
        put.disconnect()
    except Exception:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception:
        pass
    try:
        adk.run_until_disconnected()
    except Exception:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception:
        pass
    try:
        edk.run_until_disconnected()
    except Exception:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception:
        pass
    try:
        sid.run_until_disconnected()
    except Exception:
        pass
    try:
        shy.run_until_disconnected()
    except Exception:
        pass
    try:
        aan.run_until_disconnected()
    except Exception:
        pass
    try:
        ake.run_until_disconnected()
    except Exception:
        pass
    try:
        eel.run_until_disconnected()
    except Exception:
        pass
    try:
        khu.run_until_disconnected()
    except Exception:
        pass
    try:
        shi.run_until_disconnected()
    except Exception:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception:
        pass
    try:
        dav.run_until_disconnected()
    except Exception:
        pass
    try:
        raj.run_until_disconnected()
    except Exception:
        pass
    try:
        put.run_until_disconnected()
    except Exception:
        pass
