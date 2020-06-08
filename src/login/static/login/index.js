

function printChecked(){
    let items=document.getElementsByName('ckb');
    let selectedItems="";
    for(let i=0; i<items.length; i++){
        if(items[i].type=='checkbox' && items[i].checked==true)
            selectedItems+=items[i].value+"\n";
    }
    alert('Potvrdite prijavu za sledeće ispite: ' + '\n' + '\n' + selectedItems);

}	


// function cbPredmeti() {
//         let checkedCheckbox = document.getElementById('cbprijava');
//         let valcb = document.getElementById('cbprijava').value;
//         let svicekiranipredmeti='';
//         let nPredmeta = document.getElementById('nazivpredmeta');
//         let datIspita = document.getElementById('datumispita');
//         let prof = document.getElementById('profesor');
//         let sem = document.getElementById('semestar');
//         let espbBodovi = document.getElementById('espb');
//         let vrPredmeta = document.getElementById('vrstapredmeta');

//         for(i=0; i<checkedCheckbox.length; i++){
//             if (checkedCheckbox[i].checked == true && valcb[i] == nPredmeta) {
    
//                 svicekiranipredmeti += nPredmeta[i] + '\n';
//             }
//         }
//         let rez = svicekiranipredmeti;
//         // for valcb

//         // localStorage.setItem('ckbpred', 'svicekiranipredmeti')

//         document.getElementById('prikazi').innerHTML = rez;

//     }
    //document.getElementById('prikazi').innerHTML = cbPredmeti;



    // function cekiraniPredmeti() {
    //     let cekirani = document.querySelector('#cbprijava');

    //     for (let i=0; i<cekirani.length; i++) {
    //         cekirani[i].checked = true;
    //     }

    //     window.onload = function() {
    //         window.addEventListener('load', this.cekiraniPredmeti, false);
    //     }
    // }


// function prikaziCekiranePredmete() {
//     let predmeti = document.getElementById('cbprijava');
//     let cekiraniPredmeti = '';

//     for(let i=0; i<predmeti.length; i++){
//         if(predmeti[i].type == 'checkbox' && predmeti[i].checked == true){
//             cekiraniPredmeti += predmeti[i].value + '\n';
//         }
//     }

//     let rezultat = cekiraniPredmeti;

//     document.getElementById('prikazi').innerHTML = rezultat;
// }


// function prikaziCP(){
//     let predmeti = document.getElementById('cbprijava');
//     let cekiraniPredmeti = '';

//         for(let i=0; i<predmeti.length; i++){
//             if(predmeti[i].type == 'checkbox' && predmeti[i].checked == true){
//                 cekiraniPredmeti += predmeti[i].value + '\n';
//             }
//         }

//     let rezultat = cekiraniPredmeti;

//     var div = document.getElementById('prikazi'), cekiraniCheckbox;

//     localStorage.setItem('cekiraniCheckbox', rezultat);

//     cekiraniCheckbox = localStorage.getItem('cekiraniCheckbox');

//     div.innerHTML = cekiraniCheckbox;
// }
