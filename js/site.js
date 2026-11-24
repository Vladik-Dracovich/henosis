const yearNode = document.getElementById("year");
if (yearNode) yearNode.textContent = new Date().getFullYear();
document.querySelectorAll('a[href^="#"]').forEach(a=>{
 a.addEventListener("click",()=>document.activeElement && document.activeElement.blur());
});