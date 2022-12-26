using System.Collections;
using System.Linq;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System;

public class Yokai
{
    public string category; 
    public string name;
    public List<string> attacks;
    public List<int> attackDMG;
    public string convo;
    public (string, (string, int)) cYes;
    public (string, (string, int)) cNo;
    public int run;
    public List<string> item;
    public int DC;
    public string intro;
    public string defeatATK;
    public Dictionary<string, string> defeatItem;
    public int health; 
}

public class Weapon
{
    public string name;
    public string info;
    public int atk;
    //public List<string> yokai;
    public ArrayList yokai;
    public int count;
    public string category; 
}

public class Heals
{
    public string name;
    public string info;
    public int healing;
    public List<string> yokai;
    public int count;
    public string category;
}


public class Curses
{
    public string name;
    public string info;
    //public (bool, int?) isHarmful; 
    public ArrayList isHarmful;
    //public ArrayList selfHarm;
    public (bool, int) selfHarm;
    public int count;
    public string category;
}


public class Directory : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void PsuedoMain()
    {
        // call read for each file
        //GetCSV("curses", "https://github.com/thumun/YokaiLand/blob/main/Curses.csv");
        //GetCSV("heals", "https://github.com/thumun/YokaiLand/blob/main/Healing.csv");
        //GetCSV("weapons", "https://github.com/thumun/YokaiLand/blob/main/weapons.csv");
        //GetCSV("yokai", "https://github.com/thumun/YokaiLand/blob/main/Monsters.csv");

    }

    //public void GetCSV(string fileName, string url)
    //{
    //    WebClient webClient = new WebClient();
    //    webClient.DownloadFile(url, fileName);
    //}

    public void ReadItems(string fileName)
    {
        //List<string> splitted = new List<string>();
        //string fileList = GetCSV("curses", "https://github.com/thumun/YokaiLand/blob/main/Curses.csv");
        //string[] tempStr;

        string[] lines = System.IO.File.ReadAllLines(fileName);

        // Display the file contents by using a foreach loop.
        foreach (string line in lines)
        {
            List<string> details = line.Split(';').ToList(); // what if I have commas... use a different delimiter?? (semicolon?) 
            List<string> temp;

            if (details[details.Count - 1] == "curse")
            {
                Curses item = new Curses();

                item.name = details[0];
                item.info = details[1];

                temp = details[2].Trim('[', ']').Split(',').ToList();
                item.isHarmful.Add(Convert.ToBoolean(temp[0]));

                int intVal = 0; 
                var a = Int32.TryParse(temp[1], out intVal);

                if (a) item.isHarmful.Add(intVal); else item.isHarmful.Add(temp[1]);
                
                //item.isHarmful = ((bool cond, int? dmg)) (Convert.ToBoolean(temp[0]), a ? intVal : null);

                temp = details[3].Trim('[', ']').Split(',').ToList();
                item.selfHarm = (Convert.ToBoolean(temp[0]), Convert.ToInt32(temp[1]));

                item.count = Convert.ToInt32(details[4]);
                item.category = details[details.Count - 1];
            }
            else if (details[details.Count - 1] == "weapon"){
                Weapon item = new Weapon();

                item.name = details[0];
                item.info = details[1];
                item.atk = Convert.ToInt32(details[2]);

                temp = details[3].Trim('{', '}').Split(',').ToList();
                item.yokai.Add(Convert.ToBoolean(temp[0]));
                temp[1].Trim('[', ']').Split(',').ToList().Select(i => item.yokai.Add(i)); // will this work if there's no commas? 

                item.count = Convert.ToInt32(details[4]);
                item.category = details[details.Count - 1];

            }
            else
            {
                Heals item = new Heals();

                item.name = details[0];
                item.info = details[1];
                item.healing = Convert.ToInt32(details[2]);

                item.yokai = details[3].Trim('[', ']').Split(',').ToList(); // will this work if there's no commas? 

                item.count = Convert.ToInt32(details[4]);
                item.category = details[details.Count - 1];
            }
        }

    }

    public void readYokai(string fileName)
    {
        string[] lines = System.IO.File.ReadAllLines(fileName);
        List<string> temp;

        // Display the file contents by using a foreach loop.
        foreach (string line in lines)
        {
            List<string> details = line.Split(';').ToList(); // what if I have commas... use a different delimiter?? (semicolon?)
            Yokai monster = new Yokai();

            monster.category = details[0];
            monster.name = details[1];
            monster.attacks = details[2].Trim('[', ']').Remove('"').Split(',').ToList();
            monster.attackDMG = (List<int>)details[3].Trim('[', ']').Split(',').ToList().Select(i => Convert.ToInt32(i)); // check this
            monster.convo = details[4];

            temp = details[5].Trim('[', ']').Split(',').ToList();
            monster.cYes = (temp[0], (temp[1], Convert.ToInt32(temp[2])));

            temp = details[6].Trim('[', ']').Split(',').ToList();
            monster.cNo = (temp[0], (temp[1], Convert.ToInt32(temp[2])));

            monster.run = Convert.ToInt32(details[7]);
            monster.item = details[8].Trim('[', ']').Remove('"').Split(',').ToList();
            monster.DC = Convert.ToInt32(details[9]);
            monster.intro = details[10];
            monster.defeatATK = details[11];

            // to get below to work need to change logic in csv !!
            // may need to rethink data structure...
            temp = details[12].Trim('[', ']').Remove('"').Split(',').ToList();
            for (int i = 0; i < temp.Count; i += 2)
            {
                monster.defeatItem.Add(temp[0], temp[1]);
            }
            
            //monster.defeatItem = {key, val};

            monster.health = Convert.ToInt32(details[details.Count - 1]);
        }
    }
}
