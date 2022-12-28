using System.Collections;
using System.Linq;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System;
using NReco.Csv;
using System.IO;

public class Yokai
{
    public string category; 
    public string name;
    public List<string> attacks = new List<string>();
    public List<int> attackDMG = new List<int>();
    public string convo;
    public (string, (string, int)) cYes;
    public (string, (string, int)) cNo;
    public int run;
    public List<string> item = new List<string>();
    public int DC;
    public string intro;
    public string defeatATK;
    public Dictionary<string, string> defeatItem = new Dictionary<string, string>();
    public int health; 
}

public class Weapon
{
    public string name;
    public string info;
    public int atk;
    //public List<string> yokai;
    public ArrayList yokai = new ArrayList();
    public int count;
    public string category; 
}

public class Heals
{
    public string name;
    public string info;
    public int healing;
    public List<string> yokai = new List<string>();
    public int count;
    public string category;
}


public class Curses
{
    public string name;
    public string info;
    //public (bool, int?) isHarmful; 
    public ArrayList isHarmful = new ArrayList();
    //public ArrayList selfHarm;
    public (bool, int) selfHarm;
    public int count;
    public string category;
}

public class Repository
{
    public static List<object> ReadItems(string fileName)
    {
        List<object> items = new List<object>(); 

        using (var streamRdr = new StreamReader(System.IO.Directory.GetCurrentDirectory()+@"/Assets/Data/"+fileName+".csv"))
        {
            var csvReader = new CsvReader(streamRdr, ",");
            csvReader.Read(); 
            while (csvReader.Read())
            {
                //for (int i = 0; i < csvReader.FieldsCount; i++)
                //{
                    //Debug.Log(csvReader[i]);

                    int j = 0; 

                    List<string> temp = new List<string>();

                    Debug.Log(csvReader[j]);
                    if (csvReader[j + 5] == "curse")
                    {
                        Curses item = new Curses();

                        item.name = csvReader[j];
                        item.info = csvReader[j + 1];

                        temp = csvReader[j + 2].Trim('[', ']').Split(',').ToList();
                        item.isHarmful.Add(Convert.ToBoolean(temp[0]));

                        int intVal = 0;
                        var a = Int32.TryParse(temp[1], out intVal);

                        if (a) item.isHarmful.Add(intVal); else item.isHarmful.Add(temp[1]);

                        //item.isHarmful = ((bool cond, int? dmg)) (Convert.ToBoolean(temp[0]), a ? intVal : null);

                        temp = csvReader[j + 3].Trim('[', ']').Split(',').ToList();
                        item.selfHarm = (Convert.ToBoolean(temp[0]), Convert.ToInt32(temp[1]));

                        item.count = Convert.ToInt32(csvReader[j + 4]);
                        item.category = csvReader[j + 5];

                        items.Add(item);
                    }
                    else if (csvReader[j + 5] == "weapon")
                    {
                        Weapon item = new Weapon();

                        item.name = csvReader[j];
                        item.info = csvReader[j + 1];
                        item.atk = Convert.ToInt32(csvReader[j + 2]);

                        temp = csvReader[j + 3].Trim('{', '}').Split(',').ToList();
                        item.yokai.Add(Convert.ToBoolean(temp[0]));
                        temp[1].Trim('[', ']').Split(',').ToList().Select(j => item.yokai.Add(j)); 

                        item.count = Convert.ToInt32(csvReader[j + 4]);
                        item.category = csvReader[j + 5];

                        items.Add(item);
                    }
                    else
                    {
                        Heals item = new Heals();

                        item.name = csvReader[j];
                        item.info = csvReader[j + 1];
                        item.healing = Convert.ToInt32(csvReader[j + 2]);

                        item.yokai = csvReader[j + 3].Trim('[', ']').Split(',').ToList(); 

                        item.count = Convert.ToInt32(csvReader[j + 4]);
                        item.category = csvReader[j + 5];

                        items.Add(item);
                    }

                //}
            }
        }

        return items;
    }

    public static List<object> readYokai(string fileName)
    {
        //string[] lines = System.IO.File.ReadAllLines(fileName);
        //List<string> temp;

        //foreach (string line in lines)
        //{

        List<object> monsters = new List<object>();

        using (var streamRdr = new StreamReader(System.IO.Directory.GetCurrentDirectory() + @"/Assets/Data/" + fileName + ".csv"))
        {
            var csvReader = new CsvReader(streamRdr, ",");
            csvReader.Read();
            while (csvReader.Read())
            {
                //List<string> details = line.Split(';').ToList(); // what if I have commas... use a different delimiter?? (semicolon?)
                Yokai monster = new Yokai();
                List<string> temp = new List<string>();

                int j = 0;

                monster.category = csvReader[j];
                monster.name = csvReader[j+1];
                monster.attacks = csvReader[j+2].Trim('[', ']').Remove('"').Split(',').ToList();
                monster.attackDMG = (List<int>)csvReader[j+3].Trim('[', ']').Split(',').ToList().Select(i => Convert.ToInt32(i)); // check this
                monster.convo = csvReader[j+4];

                temp = csvReader[j+5].Trim('[', ']').Split(',').ToList();
                monster.cYes = (temp[0], (temp[1], Convert.ToInt32(temp[2])));

                temp = csvReader[j+6].Trim('[', ']').Split(',').ToList();
                monster.cNo = (temp[0], (temp[1], Convert.ToInt32(temp[2])));

                monster.run = Convert.ToInt32(csvReader[j+7]);
                monster.item = csvReader[j+8].Trim('[', ']').Remove('"').Split(',').ToList();
                monster.DC = Convert.ToInt32(csvReader[j+9]);
                monster.intro = csvReader[j+10];
                monster.defeatATK = csvReader[j+11];

                temp = csvReader[j+12].Trim('[', ']').Remove('"').Split(',').ToList();
                for (int i = 0; i < temp.Count - 1; i += 2)
                {
                    monster.defeatItem.Add(temp[i], temp[i + 1]);
                }

                monster.health = Convert.ToInt32(csvReader[j+13]);

                monsters.Add(monster);
            }
            return monsters; 
        }
    }
}
