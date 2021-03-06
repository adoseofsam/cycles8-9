import { IonButton, IonIcon, IonItem, IonLabel, IonList, IonMenuButton, IonToggle } from "@ionic/react";
import { logoWindows, moon } from "ionicons/icons";
import React, {useEffect, useState} from "react";




export const NavButtons = (props:any) =>{
    const [show, setShow] = useState<boolean>(props.userInfo.role == 'Admin' ? false : true);
    const [mQuery, setMQuery] = React.useState<any>({
        matches: window.innerWidth > 600 ? true :false,
        
    });

    const [wSize, setwSize] = useState<boolean>(false)

    function checkSize(){

        let size = window.innerWidth > 600 ? true :false;
        setwSize(size);
    }



useEffect (() => {
    // let mediaQuery = window.matchMedia("(min-widow:600px)");
    // mediaQuery.addEventListener("resize",setMQuery);

    window.addEventListener('resize', checkSize);
    // console.log("here");
    // this is the cleanup function to remove the listener
    //return () => mediaQuery.removeEventListener("resize",setMQuery);
}, []);
//let mediaQuery = window.matchMedia("(min-widow:600px)");
//  console.log(wSize);
//  console.log(mQuery.matches);
//  console.log("I am right here");
return (
    <div>
        {mQuery && !wSize ? (
            <IonMenuButton/> ) : (
                <>
                
                <IonButton  color = "none" routerLink={"/home"}>Home</IonButton>
                <IonButton  color = "none" routerLink={"/createEvent"}>Create Event</IonButton>
                { show && props.userInfo.role === 'Admin'?
                <IonButton  color = "none" routerLink={"/reviewEvent"}>Review Event</IonButton>
                : ""}
                <IonButton  color = "none" routerLink={"/login"}>Logout</IonButton>
                </>
            )
        }
    </div>
);


};