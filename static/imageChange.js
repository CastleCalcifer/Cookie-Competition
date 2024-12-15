var imageList = ["https://www.jocooks.com/wp-content/uploads/2021/12/sugar-cookies-1-17.jpg",
    "https://assets.bonappetit.com/photos/5ca534485e96521ff23b382b/1:1/w_2560%2Cc_limit/chocolate-chip-cookie.jpg",
    "https://www.thepkpway.com/wp-content/uploads/2017/12/gingerbread-cookies-3f.jpg",
    "https://thelittlevintagebakingcompany.com/wp-content/uploads/2023/03/Sprinkle-Sugar-Cookies-15.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh4k251xFF_9ijySYa4PoRBwdRDOixcZmkhw&s",
    "https://bakingamoment.com/wp-content/uploads/2023/12/IMG_0082-red-velvet-chocolate-chip-cookies.jpg"
];

document.querySelector('form').addEventListener('change', e =>{
        selectedDivID = e.target.parentElement.id;
        document.getElementById("awardImage" + selectedDivID).src = imageList[document.getElementById("awardDropdown" + selectedDivID).selectedIndex]
});