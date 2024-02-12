var today = new Date();
			var birthDate = new Date("2023-10-05");
            var day = today.getDate() - birthDate.getDate();
			var age = today.getFullYear() - birthDate.getFullYear();
            var yr = today.getFullYear();
            var mn = today.getMonth() + 1;
			var monthDiff = today.getMonth() - birthDate.getMonth();
            if(mn==5||mn==7||mn==10||mn==12){ dy = 30}
            else if(mn==3){dy = 28}
            else {dy = 31}
            if (day <0){day +=dy; monthDiff--;}
			if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
				age--;
			}
            if (monthDiff < 0){monthDiff +=12;}
			document.getElementById("age").innerText = age +"  Year  "+ monthDiff +"  Month  "+ day +"  Day\nSince  05  October  2023";
