function check_admin(){
    return sessionStorage.getItem("email") === "keeganasmith2003@gmail.com"
}

export { check_admin }