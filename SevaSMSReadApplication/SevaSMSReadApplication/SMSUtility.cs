using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Collections.Specialized;
using System.IO;
using System.Web;

namespace SevaSMSReadApplication
{
    class SMSUtility
    {

        string username = "makarand.kurkute@gmail.com";
        string hash = "Abcd1234";
        string inbox_id = "10";

        public string getMessages()
        {
            String result;
            String url = "http://api.textlocal.in/get_messages/?username=" + username + "&hash=" + hash + "&inbox_id=" + inbox_id;
            //refer to parameters to complete correct url string

            StreamWriter myWriter = null;
            HttpWebRequest objRequest = (HttpWebRequest)WebRequest.Create(url);

            objRequest.Method = "POST";
            objRequest.ContentLength = Encoding.UTF8.GetByteCount(url);
            objRequest.ContentType = "application/x-www-form-urlencoded";
            try
            {
                myWriter = new StreamWriter(objRequest.GetRequestStream());
                myWriter.Write(url);
            }
            catch (Exception e)
            {
                return e.Message;
            }
            finally
            {
                myWriter.Close();
            }

            HttpWebResponse objResponse = (HttpWebResponse)objRequest.GetResponse();
            using (StreamReader sr = new StreamReader(objResponse.GetResponseStream()))
            {
                result = sr.ReadToEnd();
                // Close and clean up the StreamReader
                sr.Close();
            }

            return result;
        }

        public string sendSMS(string strMsg, object number)
        {
            String message = HttpUtility.UrlEncode(strMsg);
            using (var wb = new WebClient())
            {
                byte[] response = wb.UploadValues("http://api.textlocal.in/send/", new NameValueCollection()
                {
                {"username" ,username },
                {"hash" , hash},
                {"numbers" , number.ToString() },
                {"message" , message},
                {"sender" , "TXTLCL"}
                });
                string result = System.Text.Encoding.UTF8.GetString(response);
                return result;
            }
        }
    }

}
