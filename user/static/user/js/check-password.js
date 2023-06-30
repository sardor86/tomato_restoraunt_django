function LoginVerifyPassword()
{
    if (document.getElementById('login_password').value.length < 8)
    {
        document.getElementById('login_errors').innerHTML = '<div class="alert alert-error"><span>ERROR</span>: password is invalid</div>'
        return false
    }
    return true
}