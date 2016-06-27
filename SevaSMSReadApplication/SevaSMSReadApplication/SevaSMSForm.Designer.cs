namespace SevaSMSReadApplication
{
    partial class SevaSMSForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.TimerStart = new System.Windows.Forms.Button();
            this.TimerStop = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // TimerStart
            // 
            this.TimerStart.Location = new System.Drawing.Point(67, 41);
            this.TimerStart.Name = "TimerStart";
            this.TimerStart.Size = new System.Drawing.Size(112, 23);
            this.TimerStart.TabIndex = 0;
            this.TimerStart.Text = "Srart SMS Service";
            this.TimerStart.UseVisualStyleBackColor = true;
            this.TimerStart.Click += new System.EventHandler(this.button1_Click);
            // 
            // TimerStop
            // 
            this.TimerStop.Location = new System.Drawing.Point(179, 41);
            this.TimerStop.Name = "TimerStop";
            this.TimerStop.Size = new System.Drawing.Size(129, 23);
            this.TimerStop.TabIndex = 1;
            this.TimerStop.Text = "Stop SMS Service";
            this.TimerStop.UseVisualStyleBackColor = true;
            this.TimerStop.Click += new System.EventHandler(this.button1_Click_1);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(67, 70);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 13);
            this.label1.TabIndex = 2;
            // 
            // SevaSMSForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(377, 127);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.TimerStop);
            this.Controls.Add(this.TimerStart);
            this.Name = "SevaSMSForm";
            this.Text = "SEWA SMS Service";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button TimerStart;
        private System.Windows.Forms.Button TimerStop;
        private System.Windows.Forms.Label label1;
    }
}

