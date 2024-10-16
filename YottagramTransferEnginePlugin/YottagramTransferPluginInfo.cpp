/*
    Copyright (C) 2018 Michał Szczepaniak

    This file is part of Yottagram.

    Yottagram is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Yottagram is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Yottagram.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "YottagramTransferPluginInfo.h"
#include <QDebug>

YottagramPluginInfo::YottagramPluginInfo(): m_ready(false)
{
}

YottagramPluginInfo::~YottagramPluginInfo()
{

}

QList<SharingMethodInfo> YottagramPluginInfo::info() const
{
    return m_infoList;
}

void YottagramPluginInfo::query()
{
    SharingMethodInfo info;

    QStringList capabilities;
    capabilities << QLatin1String("*");

    info.setDisplayName(QLatin1String("Yottagram"));
    info.setMethodId(QLatin1String("YottagramTransferEnginePlugin"));
    info.setShareUIPath(QLatin1String("/usr/share/nemo-transferengine/plugins/YottagramShare.qml"));
    info.setMethodIcon(QLatin1String("/usr/share/icons/hicolor/172x172/apps/yottagram.png"));
    info.setCapabilities(capabilities);
    m_infoList << info;
    m_ready = true;
    emit infoReady();
}

bool YottagramPluginInfo::ready() const
{
    return m_ready;
}
