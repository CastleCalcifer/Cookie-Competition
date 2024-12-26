
const cookieImages = new Map();
cookieImages.set("---", "https://www.jocooks.com/wp-content/uploads/2021/12/sugar-cookies-1-17.jpg")
cookieImages.set("Chocolate Grocery Store", "https://cdn.discordapp.com/attachments/870351415942471760/1321600930604519518/PXL_20241225_220945877.jpg?ex=676dd448&is=676c82c8&hm=7e9719d858e73d96d9965bda02f0586351f828008230a62e3fa2081690f5200c&")
cookieImages.set("Gingerbread Royal Icing", "https://cdn.discordapp.com/attachments/377606980900225024/1320857314345095229/20241223_145423.jpg?ex=676dc2bc&is=676c713c&hm=a483f7227775ddafdd70d766fd317dca65f01500cc8ff74b7940d43ee28ad816&")
cookieImages.set("Tiramisu Cookie", "https://cdn.discordapp.com/attachments/773374590650941492/1319842963181801493/IMG_4377.jpg?ex=676d5dcb&is=676c0c4b&hm=5d1c310beef80047e565d7024fcc93dd56baa916f59c0fcdaa4638c155ece6e6&")
cookieImages.set("Italian Ricotta", "https://cdn.discordapp.com/attachments/877364364972269608/1321183272352616521/IMG_1945.jpg?ex=676da0ce&is=676c4f4e&hm=eba7240249f5b3bde4c102e2e82d65e1e48802818a2d04c0e902322786fb8b96&")
document.querySelector('form').addEventListener('change', e =>{
        selectedDivID = e.target.parentElement.id;
        console.log(document.getElementById("awardDropdown" + selectedDivID).value)
        document.getElementById("awardImage" + selectedDivID).src = cookieImages.get(document.getElementById("awardDropdown" + selectedDivID).value)
});