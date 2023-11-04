*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input new Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jami  jami1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  jami1234
    Output Should Contain  name already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  jami1234
    Output Should Contain  name must be atleast 3 chr

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  kalle123  jami1234
    Output Should Contain  username can only contain alphabets
Register With Valid Username And Too Short Password
    Input Credentials  kalle123  123456
    Output Should Contain  password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jami  jaminsalis
    Output Should Contain  Insufficient password

*** Keywords ***
Create User And Input new Command
    Create User  kalle  kalle123
    Input new Command