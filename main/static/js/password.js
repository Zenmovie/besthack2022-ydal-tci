function show_pwd() {
    var x = document.getElementById("passwd");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
    var x = document.getElementById("passwd1");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}