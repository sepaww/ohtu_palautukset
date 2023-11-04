
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  jami
    Set Password  jami1234
    Set Password Confirmation  jami1234
    Submit Registeration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ja
    Set Password  jami1234
    Set Password Confirmation  jami1234
    Submit Registeration
    Registration Should Fail With Message  name must be atleast 3 chr

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  jami
    Set Password  jamijami
    Set Password Confirmation  jamijami
    Submit Registeration
    Registration Should Fail With Message  Insufficient password

Register With Nonmatching Password And Password Confirmation
    Set Username  jami
    Set Password  jami1234
    Set Password Confirmation  jami12345
    Submit Registeration
    Registration Should Fail With Message  password and password confirmation do not match


Login After Successful Registration
    Set Username  jami
    Set Password  jami1234
    Set Password Confirmation  jami1234
    Submit Registeration
    Go To Login Page
    Set Username  jami
    Set Password  jami1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  jamii
    Set Password  jami1234
    Set Password Confirmation  jami12345
    Submit Registeration
    Go To Login Page
    Set Username  jamii
    Set Password  jami1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password





*** Keywords ***

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Submit Registeration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Registration Should Succeed
    Welcome Page Should Be Open

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open



