function click1(e){
    elemen = e.currentTarget;
    console.log(elemen)
    var nama = "andila";
    document.getElementById("nama").innerHTML = "" + nama;
    
}

function click2(e){
    elemen = e.currentTarget;
    var nama1 = "andila2";
    document.getElementById("nama").innerHTML = "" + nama1;
}

function fungsi_reset(){
    document.getElementById("nama").innerHTML ="";
}

function fungsi_click1(e){
    elemen = e.currentTarget;
    console.log(elemen)
    var nama = "andila";
    document.getElementById("nama").innerHTML = "nama saya adalah " + nama;
    
}

function fungsi_click2(e){
    elemen = e.currentTarget;
    var nama1 = "andila2";
    document.getElementById("nama2").innerHTML = "nama saya adalah  " + nama1;
}

function fungsi_reset(){
    document.getElementById("nama").innerHTML ="";
    document.getElementById("nama2").innerHTML ="";
}

function fungsi_5(e){
    let elemen = e.currentTarget;
    elemen.style.bagroundcolor ="yellow";
    console.log(elemen)
    let nama = "andila";
    document.getElementById("nama").innerHTML = "nama saya adalah " + nama;
    
}

function fungsi_6(e){
    let elemen = e.currentTarget;
    var nama1 = "andila2";
    document.getElementById("nama").innerHTML = "namaku  " + nama1;
}

function kalkulator_tambah() {
    let a = parseInt(document.getElementById("nilaiA").value);
    let b = parseInt(document.getElementById("nilaiB").value);

    let hasil = a + b;

    document.getElementById("hasil").innerHTML = hasil;
}

function setOperator(op) {
    operator = op;
}

function kalkulator_hitung(e) {
    e.preventDefault();

    let a = parseInt(document.getElementById("angka1").value);
    let b = parseInt(document.getElementById("angka2").value);
    let hasil = 0;

    if (operator === "+") {
        hasil = a + b;
    } else if (operator === "-") {
        hasil = a - b;
    }

    document.getElementById("hasil").innerHTML =
        "<p><b>Hasil: " + hasil + "</b></p>";
}

 function setOperator(op) {
            operator = op;
        }

        function perhitungan(e) {
            e.preventDefault();

            let a = parseFloat(document.getElementById("angka1").value);
            let b = parseFloat(document.getElementById("angka2").value);
            let hasil;

            if (operator === "+") {
                hasil = a + b;
            } else if (operator === "-") {
                hasil = a - b;
            } else if (operator === "*") {
                hasil = a * b;
            } else if (operator === "/") {
                if (b === 0) {
                    hasil = "Tidak bisa dibagi 0";
                } else {
                    hasil = a / b;
                }
            }

            document.getElementById("hasil").innerHTML =
                "<p><b>Hasil: " + hasil + "</b></p>";
        }

let mode = "dolar"; // dolar -> rupiah

function konversi1() {
    let nilai = parseFloat(document.getElementById("nilai").value);
    let hasil = 0;

    if (mode === "dolar") {
        hasil = nilai * 15000;
        document.getElementById("hasil").innerHTML =
            "Rupiah " + hasil;
    } else {
        hasil = nilai / 15000;
        document.getElementById("hasil").innerHTML =
            "Dollar " + hasil;
    }
}

function tukar1() {
    let label = document.getElementById("label");
    let hasil = document.getElementById("hasil");

    if (mode === "dolar") {
        mode = "rupiah";
        label.innerHTML = "Rupiah";
        hasil.innerHTML = "Dollar 1";
        document.getElementById("nilai").value = 15000;
    } else {
        mode = "dolar";
        label.innerHTML = "Dollar";
        hasil.innerHTML = "Rupiah 15000";
        document.getElementById("nilai").value = 1;
    }
}
let timer = null;

function konversi3() {
    clearTimeout(timer);

    timer = setTimeout(() => {
        let c = document.getElementById("celcius").value;

        if (c === "") {
            document.getElementById("hasil").innerHTML = "Fahrenheit";
            return;
        }

        let f = (c * 9 / 5) + 32;

        document.getElementById("hasil").innerHTML =
            "Fahrenheit " + f;
    }, 500); 
}

function cekKelulusan() {
    let batas = parseInt(document.getElementById("batas").value);
    let nilai = parseInt(document.getElementById("nilai").value);
    let hasil = document.getElementById("hasil");

    if (isNaN(nilai) || isNaN(batas)) {
        hasil.innerHTML = "Masukkan nilai dengan benar";
        return;
    }

    if (nilai >= batas) {
        hasil.innerHTML = "Lulus";
    } else {
        hasil.innerHTML = "Tidak Lulus";
    }
}

const btnUtama = document.getElementById('btnUtama');
const containerMenu = document.getElementById('containerMenu');


btnUtama.onclick = function() {
   
    if (containerMenu.style.display === 'none') {
        containerMenu.style.display = 'block';
    } else {
        containerMenu.style.display = 'none';
    }
};

