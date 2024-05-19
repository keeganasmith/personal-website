function check_admin(){
    console.log("got to check admin")
    return sessionStorage.getItem("email") === "keeganasmith2003@gmail.com"
}

export { check_admin }