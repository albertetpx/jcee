window.onload = function () {
    initCalendar();
    // initCalendarNextYear();
    initSchoolYear();
    // initNextSchoolYear();
    initHolidays();

    // Add listeners
    document.getElementById("calculateButton").addEventListener('click', updatePracticeEnd);
    // document.getElementById("calendarToggleButton").addEventListener('click', toggleCalendar);
    document.getElementById("addHolidayButton").addEventListener('click', displayAddHolidayModal);
    document.getElementById("addHolidaySubmitButton").addEventListener('click', addHolidayRequest);
    document.getElementById("removeHolidayButton").addEventListener('click', displayRemoveHolidayModal);
    document.getElementById("removeHolidaySubmitButton").addEventListener('click', removeHolidayRequest);
    document.getElementById("closeAddHolidayButton").addEventListener('click', closeAddHolidayModal);
    document.getElementById("closeRemoveHolidayButton").addEventListener('click', closeRemoveHolidayModal);
    document.getElementById("calendarMenuButton").addEventListener('click', showCalendarConfirm);
    document.getElementById("closeCalendarMenuButton").addEventListener('click', closeCalendarMenuModal);
}


function updateHolidayList(holidayList) {
    // remove current holidays from holidays dropdown
    let holidaysDroplist = document.getElementById("holidays");
    let holidays = Array.from(holidaysDroplist.children);
    for (let holiday of holidays) {
        holiday.remove();
    }
    // update holidays in holidays dropdown
    for (let holiday of holidayList) {
        let option = document.createElement("option");
        option.value = holiday[0];
        option.classList.add(holiday[2]);
        option.innerHTML = `${holiday[0]}-${holiday[1]}`
        holidaysDroplist.append(option);
    }
    //refresh calendar
    initHolidays();
    // close modal
    closeAddHolidayModal();
    closeRemoveHolidayModal();
    return
}

function showCalendarConfirm(){
    if(confirm("Atenció, si vols fer canvis en el calendari, el càlcul actual de pràctiques es perdrà. Prem Cancel·lar si no vols que es perdi.")){
        displayCalendarMenuModal();
    }
}

function displayCalendarMenuModal() {
    document.getElementsByClassName("calendarMenuModal")[0].style.display = 'block';
    document.getElementById("page-mask").style.display = 'block';
}

function closeCalendarMenuModal() {
    document.getElementsByClassName("calendarMenuModal")[0].style.display = 'none';
    document.getElementById("page-mask").style.display = 'none';
}

function displayRemoveHolidayModal() {
    // get selected holiday
    document.getElementsByClassName("removeHolidayModal")[0].style.display = 'block';
    let holidaysDropdown = document.getElementById("holidays");
    let holidayDate = holidaysDropdown.options[holidaysDropdown.selectedIndex].value;
    let holidayName = holidaysDropdown.options[holidaysDropdown.selectedIndex].innerHTML;
    holidayName = holidayName.replace(holidayDate, '');
    holidayName = holidayName.replace('-', '');
    // show selected holiday in modal form
    document.getElementById("removeHolidayFormName").value = holidayName;
    document.getElementById("removeHolidayFormDate").value = holidayDate;
}

function closeRemoveHolidayModal() {
    document.getElementsByClassName("removeHolidayModal")[0].style.display = 'none';
}

function displayAddHolidayModal() {
    document.getElementsByClassName("addHolidayModal")[0].style.display = 'block';
}

function closeAddHolidayModal() {
    document.getElementsByClassName("addHolidayModal")[0].style.display = 'none';
}

function addHolidayRequest() {
    let xmlhttp = new XMLHttpRequest();

    xmlhttp.open('post', '/crearFestivo');
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            holidayList = JSON.parse(this.responseText);
            updateHolidayList(holidayList);
        }
    }
    xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    let name = document.getElementById("addHolidayFormName").value;
    let date = document.getElementById("addHolidayFormDate").value;
    let type = document.getElementById("addHolidayFormType").value;
    payload = `name=${name}&date=${date}&type=${type}`
    xmlhttp.send(payload);
}

function removeHolidayRequest() {
    let xmlhttp = new XMLHttpRequest();

    xmlhttp.open('post', '/eliminarFestivo');
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            holidayList = JSON.parse(this.responseText);
            updateHolidayList(holidayList);
        }
    }
    xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    let name = document.getElementById("removeHolidayFormName").value;
    let date = document.getElementById("removeHolidayFormDate").value;
    payload = `name=${name}&date=${date}`
    xmlhttp.send(payload);
}

function toggleCalendar(e) {
    let calendarA = document.getElementById("calendarA");

    if (calendarA.style.display != "none") {
        calendarA.style.display = "none";
    }
    else {
        calendarA.style.display = "flex";
        e.target.style.backgroundImage = rightArrowURL;
    }
    let calendarB = document.getElementById("calendarB");
    if (calendarB.style.display != "flex") {
        calendarB.style.display = "flex";
        e.target.style.backgroundImage = leftArrowURL;
    }
    else {
        calendarB.style.display = "none";
    }
}

function updatePracticeEnd(e) {
    e.preventDefault();
    // Leer último día del curso (de momento a mano)
    let schoolYearEnd = new Date(document.getElementById("schoolYearEnd").value);
    console.log(schoolYearEnd);

    // Resetear días de prácticas del calendario
    let practiceDays = Array.from(document.getElementsByClassName('practiceDay'));
    practiceDays.forEach((element) => {
        element.classList.remove('practiceDay');
        element.classList.remove("practiceStartDay")
        element.classList.remove("practiceMaxDay")
    });

    let pendingHours = document.getElementById("pendingHours");
    pendingHours.value = 0;
    pendingHours.style.color = 'black';

    let practiceStart = new Date(document.getElementById("practiceStart").value);

    let practiceHours = document.getElementById("practiceHours").value;

    if (practiceHours == 0) {
        window.alert("Introdueixi el número d'hores de pràctiques.");
        return;
    }
    let hoursDL = parseFloat(document.getElementById("horariDL").value);
    let hoursDM = parseFloat(document.getElementById("horariDM").value);
    let hoursDX = parseFloat(document.getElementById("horariDX").value);
    let hoursDJ = parseFloat(document.getElementById("horariDJ").value);
    let hoursDV = parseFloat(document.getElementById("horariDV").value);

    let calendarDays = Array.from(document.getElementsByClassName("calendarDay"));
    let dayCount = 0;

    for (let calendarDay of calendarDays) {
        let date = new Date(calendarDay.id);

        if (+date >= +practiceStart &&
            !calendarDay.classList.contains("holiday") &&
            !calendarDay.classList.contains("summerHoliday") &&
            !calendarDay.classList.contains("xmasHoliday") &&
            !calendarDay.classList.contains("easterHoliday") &&
            !calendarDay.classList.contains("weekend") &&
            !calendarDay.classList.contains("nonLectiveDay")) {

            calendarDay.classList.add("practiceDay");
            weekday = date.getDay();
            document.getElementById("practiceEnd").value = date.toISOString().slice(0, 10);
            dayCount += 1;
            if (weekday == 1) { practiceHours = practiceHours - hoursDL; }
            else if (weekday == 2) { practiceHours = practiceHours - hoursDM; }
            else if (weekday == 3) { practiceHours = practiceHours - hoursDX; }
            else if (weekday == 4) { practiceHours = practiceHours - hoursDJ; }
            else if (weekday == 5) { practiceHours = practiceHours - hoursDV; }
            console.log(dayCount, practiceHours);
            if (practiceHours <= 0) {
                break;
            }
            if (date >= schoolYearEnd) {
                console.log("School year end!!!");
                calendarDay.classList.add('practiceMaxDay');
                let pendingHours = document.getElementById("pendingHours");
                pendingHours.value = practiceHours;
                pendingHours.style.color = 'red';
                break;
            }
        }
    }
    return;
}

function updateTotalHours() {
    //TBD: automatically fill in hours input when DUAL/FCT selected
}

function initSchoolYear() {
    let calendarDays = Array.from(document.getElementsByClassName("calendarDay"));
    let schoolYearStart = new Date(document.getElementById("schoolYearStart").value);
    let schoolYearEnd = new Date(document.getElementById("schoolYearEnd").value);
    let xmasStart = new Date(document.getElementById("xmasStart").value);
    let xmasEnd = new Date(document.getElementById("xmasEnd").value);
    let easterStart = new Date(document.getElementById("easterStart").value);
    let easterEnd = new Date(document.getElementById("easterEnd").value);

    // Mark out off-season, weekends
    for (let calendarDay of calendarDays) {
        let date = new Date(calendarDay.id);
        if (date < schoolYearStart || date > schoolYearEnd) {
            calendarDay.classList.add("summerHoliday");
        }
        // else if (xmasStart <= date && date <= xmasEnd) {
        //     calendarDay.classList.add("nonLectiveDay");
        // }
        // else if (easterStart <= date && date <= easterEnd) {
        //     calendarDay.classList.add("nonLectiveDay");
        // }
        else if (date.getDay() == 6) {
            calendarDay.classList.add("weekend");
        }
        else if (date.getDay() == 0) {
            calendarDay.classList.add("weekend");
        }
    }
}

function initHolidays() {
    // clean calendar
    let oldHolidays = Array.from(document.getElementsByClassName("holiday"));
    for (let holiday of oldHolidays) {
        holiday.classList.remove("holiday");
        holiday.classList.remove("nonLectiveDay");
    }

    let holidays = Array.from(document.getElementById("holidays").children);

    for (let holiday of holidays) {
        holidayDate = holiday.value;
        let cell = document.getElementById(`${holidayDate}`);
        if (holiday.classList.contains("national")) {
            cell.classList.add("holiday");
        }
        else if (holiday.classList.contains("school")) {
            cell.classList.add("nonLectiveDay");
        }
    }
}

function initCalendar() {

    // TODO: BACKEND
    let yearIni = 2022;
    let initDate = `${yearIni}-09-01`;
    let initDay = new Date(initDate);

    // Iteration through monthly calendars
    for (monthindex in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) {
        let monthGrid = Array.from(document.getElementsByClassName("calendar-grid")[monthindex].children);
        // Iteration on month days
        let date = initDay;
        let weekday = initDay.getDay();
        month = date.getMonth()
        for (const [cellindex, daycell] of monthGrid.entries()) {
            if (date.getMonth() != month) break;
            if (cellindex > (6 + weekday - 1)) { // Heading cells
                // Month day cells
                daycell.innerHTML = date.getDate();
                daycell.id = date.toISOString().slice(0, 10);
                daycell.classList.add("calendarDay");
                daycell.addEventListener('click', toggleLectiveDay);
                daycell.addEventListener('contextmenu', changePracticeStart);
                date = addOneDay(date);
            }
        }
    }
}

function toggleLectiveDay(e) {
    e.preventDefault();
    e.stopPropagation();
    if (!e.target.classList.contains("summerHoliday") &&
        !e.target.classList.contains("weekend") &&
        !e.target.classList.contains("holiday")) {

        if (e.target.classList.contains("nonLectiveDay")) {
            e.target.classList.remove("nonLectiveDay");
        }
        else {
            e.target.classList.add("nonLectiveDay");
        }
    }
}

function changePracticeStart(e) {
    e.preventDefault();
    e.stopPropagation();
    let practiceStartDay = document.getElementById("practiceStart");
    practiceStartDay.value = e.target.id;
    // e.target.classList.add("practiceStartDay")

}

function addOneDay(date) {
    date.setDate(date.getDate() + 1);
    return date;
}

// Funcitons not used
function initNextSchoolYear() {
    let calendarDays = Array.from(document.getElementsByClassName("calendarBDay"));
    // Missing information
    // let schoolYearStart = new Date(document.getElementById("schoolYearStart").value);
    // let schoolYearEnd = new Date(document.getElementById("schoolYearEnd").value);
    // let xmasStart = new Date(document.getElementById("xmasStart").value);
    // let xmasEnd = new Date(document.getElementById("xmasEnd").value);
    // let easterStart = new Date(document.getElementById("easterStart").value);
    // let easterEnd = new Date(document.getElementById("easterEnd").value);

    // Mark out off-season, xmas, easter, weekends
    for (let calendarDay of calendarDays) {
        let date = new Date(calendarDay.id);
        // TBD: missing information
        // if(date < schoolYearStart || date > schoolYearEnd){
        //     calendarDay.classList.add("summerHoliday");
        // }
        // else if(xmasStart <= date && date <= xmasEnd){
        //     calendarDay.classList.add("xmasHoliday");
        // }
        // else if(easterStart <= date && date <= easterEnd){
        //     calendarDay.classList.add("easterHoliday");
        // }
        // else if (date.getDay() == 6 || date.getDay() == 0){
        //     calendarDay.classList.add("weekend");
        // }
        if (date.getDay() == 6 || date.getDay() == 0) {
            calendarDay.classList.add("weekend");
        }
    }

    // Mark out christmas

    // Mark out easter

}

function initCalendarNextYear() {
    // TODO: BACKEND
    let yearIni = 2023;
    let initDate = `${yearIni}-09-01`;
    let initDay = new Date(initDate);

    // Iteration through monthly calendars
    for (monthindex in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) {
        let monthGrid = Array.from(document.getElementsByClassName("calendarB-grid")[monthindex].children);
        // Iteration on month days
        let date = initDay;
        let weekday = initDay.getDay();
        month = date.getMonth()
        for (const [cellindex, daycell] of monthGrid.entries()) {
            if (date.getMonth() != month) break;
            if (cellindex > (6 + weekday - 1)) { // Heading cells
                // Month day cells
                daycell.innerHTML = date.getDate();
                daycell.id = date.toISOString().slice(0, 10);
                daycell.classList.add("calendarBDay");
                date = addOneDay(date);
            }
        }
    }
}