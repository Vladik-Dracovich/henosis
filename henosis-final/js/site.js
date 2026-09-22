document.getElementById("year").textContent = new Date().getFullYear();
document.querySelectorAll('a[href^="#"]').forEach(a=>{
 a.addEventListener("click",()=>document.activeElement && document.activeElement.blur());
});