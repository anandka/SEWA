using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Newtonsoft.Json;
using System.Net;

namespace SevaSMSReadApplication
{
    public partial class SevaSMSForm : Form
    {

        static System.Timers.Timer aTimer;
        static System.DateTime UpdatedTm;
        public class Message
        {
            public string id { get; set; }
            public object number { get; set; }
            public string message { get; set; }
            public string date { get; set; }
            public object isNew { get; set; }
            public string status { get; set; }
        }

        public class RootObject
        {
            public int inbox_id { get; set; }
            public int num_messages { get; set; }
            public int min_time { get; set; }
            public int max_time { get; set; }
            public string sort_order { get; set; }
            public string sort_field { get; set; }
            public int start { get; set; }
            public int limit { get; set; }
            public List<Message> messages { get; set; }
            public string status { get; set; }
        }

        public class SearchRootObject
        {
            public string servicename { get; set; }
            public string username { get; set; }
            public string address { get; set; }
        }


        //public class AllSMSRootObject
        //{
        //    public List<RootObject> data { get; set; }
        //}

        static SMSUtility SMSObj;

        public SevaSMSForm()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SMSObj = new SMSUtility();
        }

        public static void ProcessSMSRead(String str)
        {
            var result = JsonConvert.DeserializeObject<RootObject>(str);
            if (result.messages != null)
            {
                foreach (Message Msg in result.messages)
                {
                    UpdatedTm = DateTime.Now.AddSeconds(-15);
                    DateTime dt = Convert.ToDateTime(Msg.date);
                    int Interresult = DateTime.Compare(UpdatedTm, dt);
                    //if (Interresult < 0)
                    {
                        if (Msg.message.ToLower().Contains("register"))
                        {
                            if (RegisterSEWAUser(Msg))
                            {

                            }
                        }
                        else if (Msg.message.ToLower().Contains("search"))
                        {
                            SearchSEWARequest(Msg);
                        }
                    }
                }    
            }
        }

        public static bool RegisterSEWAUser(Message Msg)
        {   
            //string url = "http://192.168.0.133:5000/smsregister/" + Msg.number.ToString() + "/" + "411037";
            //var request = (HttpWebRequest)WebRequest.Create(url);
            //request.GetResponse();
            string[] words = Msg.message.Split(' ');
            string url = "http://192.168.0.133:5000/smsregister/" + Msg.number.ToString() + "/" + words[2];
            WebRequest request = HttpWebRequest.Create(url);
            WebResponse response = request.GetResponse();
            System.IO.StreamReader reader = new System.IO.StreamReader(response.GetResponseStream());
            string responseText = reader.ReadToEnd();
            if (responseText.Contains("success"))
            {
                words = responseText.Split(' ');
                string str = "Congratulations! successfully registered to e-SEWA, your passward is " + words[1];
                SMSObj.sendSMS(str, Msg.number);
                return true;
            }
            return false;
        }

        public static void SearchSEWARequest(Message Msg)
        {
            //http://127.0.0.1:5000/smssearch/<category>/<pincode>
            string MsgString = "";
            string[] words = Msg.message.Split(' ');
            string url = "http://192.168.0.133:5000/smssearch/" + words[2] + "/" + words[3];
            //string url = "http://192.168.0.133:5000/smssearch/other/123";
            WebRequest request = HttpWebRequest.Create(url);
            WebResponse response = request.GetResponse();
            System.IO.StreamReader reader = new System.IO.StreamReader(response.GetResponseStream());
            string responseText = reader.ReadToEnd();
            if (responseText.Length > 1)
            {
                var Searchresult = JsonConvert.DeserializeObject<List<SearchRootObject>>(responseText);
                if (Searchresult != null)
                {                   
                    foreach (SearchRootObject SrchMsg in Searchresult)
                    {
                        MsgString += SrchMsg.servicename + " " + SrchMsg.username + " " + SrchMsg.address + Environment.NewLine;
                    }
                }
                SMSObj.sendSMS(MsgString , Msg.number);
            }
            else
                SMSObj.sendSMS("No result found", Msg.number);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            aTimer = new System.Timers.Timer();
            aTimer.Elapsed += new System.Timers.ElapsedEventHandler(OnTimedEvent);
            aTimer.Interval = 15000;
            aTimer.Enabled = true;
            TimerStart.Enabled = false;
            TimerStop.Enabled = true;
            label1.Text = "SMS service is running";
        }

        // Specify what you want to happen when the Elapsed event is raised.
        private static void OnTimedEvent(object source, System.Timers.ElapsedEventArgs e)
        {
            ProcessSMSRead(SMSObj.getMessages());
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            aTimer.Enabled = false;
            aTimer.Stop();
            TimerStart.Enabled = true ;
            TimerStop.Enabled = false ;
            label1.Text = "SMS service is stoped";
        }

    }
}
