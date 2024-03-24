const express = require("express") 
const app = express(); 
const nodemailer = require("nodemailer"); 

const sender_mail = "edkpi911@gmail.com"; 
const receiver_mail = "d13sudarsonmv@gmail.com"; 
const app_pass = "cohkocebzbjsarhg"

const transporter = nodemailer.createTransport({
    service:"gmail", 
    auth:{
        user:sender_mail,     
        pass: app_pass 
    }
}); 

// app.use(express.static("./views")); 
app.use(express.json()); 
app.use(express.urlencoded({extended:false})); 

app.get("/", (req,res) => {
    console.log("Home page Access!") 
    return "<h1>Hello, This is Mail Server</h1>"
}) 

app.post("/sendmail", (req,res) => {

    const mailoptions = {
        from:sender_mail, 
        to:receiver_mail, 
        subject:"Human Invasion Detected!" , 
        html:`<h1>Danger!!</h1><h2>Anamoly detected thorugh sensors. Invasion Detected</h2>`    
    }

    transporter.sendMail(mailoptions, (err, info) => {
        if(err){
            console.log(err); 
            res.status(500).send("Internel Server Error Occured"); 
        }else{
            console.log("Email sent: "+info.response); 
            res.status(201).send("Email Sent Successfully!!");  
        }
    });

}) 

app.listen(5000, () => {
    console.log("[SERVER STARTED]") 
})