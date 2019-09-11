function setBoxName(name)
{
    if(this.patcher.box)
    {
        this.patcher.box.varname = name;
    }
}

function getBoxName()
{
    if(this.patcher.box)
    {
        outlet(0,this.patcher.box.varname);
    }
}

function doesObjectExist(myObj)
{
  tmp =  this.patcher.getnamed(myObj);
  if(tmp)
     outlet(0,1);
  else
     outlet(0,0);
}
