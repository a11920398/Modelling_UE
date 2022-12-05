def EXTRA_plot_models_fct(model,model_name):
    '''Function to plot four (and only four!) climate models in a subplot'''
    fig=plt.figure(figsize=(18,9))
    ax0 = plt.subplot2grid((2,2),(0,0),colspan=1,rowspan=1,projection=ccrs.PlateCarree())
    ax1 = plt.subplot2grid((2,2),(0,1),colspan=1,rowspan=1,projection=ccrs.PlateCarree())
    ax2 = plt.subplot2grid((2,2),(1,0),colspan=1,rowspan=1,projection=ccrs.PlateCarree())
    ax3 = plt.subplot2grid((2,2),(1,1),colspan=1,rowspan=1,projection=ccrs.PlateCarree())
        
    axes = [ax0,ax1,ax2,ax3]
    index = [0,1,2,3]
       
    for i,j in zip(axes,index):
        data = model[model_name[j]]
        #i.coastlines()
        data.plot.pcolormesh(ax = i, cmap='coolwarm', robust=True,label='T[K]',cbar_kwargs ={'label':"Temperature [K]"})
        i.coastlines()
        i.set_extent([-160,160,-90,90])
        gl = i.gridlines(draw_labels = True)
        gl.xlabel_style = dict(fontsize=9)
        gl.ylabel_style = dict(fontsize=9,rotation=90,va='bottom',ha='center')
        gl.top_labels = False
        gl.right_labels = False
        i.set_title("mean 2 meter temperature 1970-2014 {} ".format(model_name[j]),fontsize=12)
