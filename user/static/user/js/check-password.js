function LoginVerifyPassword()
{
    if (document.getElementById('login_password').value.length < 8)
    {
        document.getElementById('login_errors').innerHTML = '<div class="alert alert-error"><span>ERROR</span>: Password is invalid</div>'
        return false
    }
    return true
}


function RegistrationVerifyPassword()
{
    let password = document.getElementById('registration_password')
    let password2 = document.getElementById('registration_password2')
    let errors = document.getElementById('registration_errors')

    if (password.value !== password2.value)
    {
        errors.innerHTML = '<div class="alert alert-error"><span>ERROR</span>: Passwords don\'t match</div>'
        return false
    }
    if (password.value.length < 8)
    {
        errors.innerHTML = '<div class="alert alert-error"><span>ERROR</span>: Password is invalid</div>'
        return false
    }

    return true
}
