$(document).ready(function () {
    
    var selectedNavLeftMenuName = localStorage.getItem("left_nav_item") ? localStorage.getItem("left_nav_item") : "zone"
    var selectedNavTopMenuName = localStorage.getItem("top_nav_item") ? localStorage.getItem("top_nav_item") : "monitor"
    var zoneParam = 1
    var paramStr = ""

    init()

    $("#side-menu li").click(function() {
        let className = $(this).attr("class")
        if(className !== "nav-header") {
            let _selectedNavLeftMenuName = $(this).attr("name")
            let _selectedNavTopMenuName = localStorage.getItem("top_nav_item")
            zoneParam = $(this).attr("value")
            paramStr = zoneParam ? "/" + zoneParam : ""

            $("#side-menu .active").removeClass("active")
            $(this).addClass("active")

            localStorage.setItem("left_nav_item", _selectedNavLeftMenuName)
            localStorage.setItem("zone_param", zoneParam)
            redirection(_selectedNavLeftMenuName, _selectedNavTopMenuName, paramStr)
        }
    })

    $("#top-menu button").click(function() {
        if($(this).hasClass("disabled")) return
        let _selectedNavTopMenuName = $(this).attr("name")
        let _selectedNavLeftMenuName = localStorage.getItem("left_nav_item")
        paramStr = _selectedNavLeftMenuName === "zone" ? "/" + localStorage.getItem("zone_param") : ""

        $("#top-menu .active").removeClass("active")
        $(this).addClass("active")

        localStorage.setItem("top_nav_item", _selectedNavTopMenuName)
        redirection(_selectedNavLeftMenuName, _selectedNavTopMenuName, paramStr)
    })

    function init() {
        let _selectedNavLeftMenuName = localStorage.getItem("left_nav_item")
        let _selectedNavTopMenuName = localStorage.getItem("top_nav_item")
        let _zoneParam = localStorage.getItem("zone_param")
        let _selectedNavLeftMenuId = _selectedNavLeftMenuName === "zone" ? _selectedNavLeftMenuName + _zoneParam : _selectedNavLeftMenuName

        $("#side-menu .active").removeClass("active")
        $("#side-menu #" + _selectedNavLeftMenuId).addClass("active")
        $("#top-menu .active").removeClass("active")
        $("#top-menu #" + _selectedNavTopMenuName).addClass("active")

    }

    function redirection(leftMenuName, topMenuName, paramStr) {
        let url = leftMenuName + "_" + topMenuName + paramStr
        window.location.href = "/" + url
    }
})